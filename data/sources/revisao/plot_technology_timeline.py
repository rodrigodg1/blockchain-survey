"""Build a descriptive publication timeline from the survey's existing extraction.

Run from any directory: python plot_technology_timeline.py
Requires matplotlib and numpy. Reads the six application tables, bibliography,
historical/recent extraction, and synthesis matrix. Never edits those inputs.
CSV outputs retain every matched field and each publication behind a cell.
Counts mean explicit descriptions, including proposals, not verified capability,
field-wide adoption, first invention, or mutually exclusive classifications.
"""
from collections import Counter
import argparse
import csv
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

REV = Path(__file__).resolve().parent
ROOT = REV.parent
# These are figure annotations, not replacements for the three original groups.
FEATURES = [
    ('HE', 'Homomorphic encryption', 'processing', r'homomorphic|Paillier|\bCKKS\b|\bFHE\b'),
    ('ABE', 'Attribute-based encryption', 'processing', r'attribute-based encryption|\b(?:CP-)?ABE\b'),
    ('PRE', 'Proxy re-encryption', 'processing', r'proxy re-encryption|\b(?-i:PRE)\b'),
    ('SEARCH', 'Searchable encryption', 'processing', r'searchable encryption|encryption with keyword search|encrypted search|keyword search over|encrypted index'),
    ('ZK', 'ZK proofs / credentials', 'processing', r'zero-knowledge|\bZK\b|zk-SNARK'),
    ('FL', 'Federated learning', 'processing', r'federated|\b(?-i:FL)\b'),
    ('DP', 'Differential privacy', 'processing', r'differential privacy|\b(?-i:LDP)\b'),
    ('SSI', 'DID / SSI', 'identity', r'\bSSI\b|\bDIDs?\b|decentralized identity|self-sovereign|\bDIDComm\b'),
    ('CREDENTIAL', 'Credentials (any format)', 'identity', r'\bcredentials?\b|\bVCs?\b'),
    ('INDY', 'Indy / Aries', 'identity', r'\bIndy\b|\bAries\b'),
    ('VERAMO', 'Veramo', 'identity', r'\bVeramo\b'),
    ('IOTA', 'IOTA Identity', 'identity', r'\bIOTA\b'),
]
TABLES = {
    'privacy-works': 'privacy', 'privacy-works-2': 'privacy',
    'consent-works': 'consent', 'consent-works-2': 'consent',
    'ssi-works-part-1': 'identity', 'ssi-works-part-2': 'identity',
}
# Fixed, non-overlapping three-year windows retain the full publication range.
# The last window ends at the survey's 30 September 2026 publication cutoff.
PERIODS = [(2015, 2017), (2018, 2020), (2021, 2023), (2024, 2026)]


def read_csv(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f))


def write_csv(path, rows):
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def extract():
    bibliography = {}
    for entry in re.split(r'(?m)^@', (ROOT / 'references-revised.bib').read_text())[1:]:
        key = re.match(r'\w+\s*\{([^,]+),', entry)
        year = re.search(r'\byear\s*=\s*[{\"](\d{4})', entry)
        if key and year:
            bibliography[key[1]] = int(year[1])
    historical = {r['citation_key']: r for r in read_csv(ROOT / 'historical-extraction.csv')}
    recent = {r['citation_key']: r for r in read_csv(REV / 'recent-extraction.csv')}
    matrix = {r['citation_key']: r for r in read_csv(REV / 'synthesis-evidence-matrix.csv')}
    records, matches = [], []
    for block in re.findall(r'\\begin\{longtable\}.*?\\end\{longtable\}', (ROOT / 'main.tex').read_text(), re.S):
        label = re.search(r'\\label\{tab:([^}]+)\}', block)
        if not label or label[1] not in TABLES:
            continue
        for line in block.splitlines():
            if not line.startswith('\\cite{'):
                continue
            key = re.match(r'\\cite\{([^}]+)\}', line)[1]
            parts = line.split(' & ')
            # Exclude Evaluation/limits: a negated property is not an observation.
            fields = {'main.tex:application': parts[1], 'main.tex:control_method': parts[2]}
            if key in historical:
                for field in ('reported_technique', 'reported_contribution'):
                    fields['historical-extraction.csv:' + field] = historical[key][field]
            if key in recent:
                for field in ('application', 'approach'):
                    fields['recent-extraction.csv:' + field] = recent[key][field]
            if key in matrix:
                for field in ('operation', 'reported_mechanism'):
                    fields['synthesis-evidence-matrix.csv:' + field] = matrix[key][field]
            row = {'citation_key': key, 'publication_year': bibliography[key],
                   'original_group': TABLES[label[1]], 'source_table': 'tab:' + label[1],
                   'source_access': matrix.get(key, {}).get('verification_status', 'inventory_only')}
            for feature, _, _, pattern in FEATURES:
                evidence = [(field, text, re.search(pattern, text, re.I)) for field, text in fields.items()]
                evidence = [(f, t, m) for f, t, m in evidence if m]
                row[feature] = int(bool(evidence))
                for field, text, match in evidence:
                    matches.append({'citation_key': key, 'publication_year': bibliography[key],
                                    'feature': feature, 'source_field': field,
                                    'matched_term': match[0], 'extracted_description': text,
                                    'source_access': row['source_access']})
            row['both_families'] = int(any(row[f] for f, _, g, _ in FEATURES if g == 'processing')
                                      and any(row[f] for f, _, g, _ in FEATURES if g == 'identity'))
            records.append(row)
    keys = {r['citation_key'] for r in records}
    assert len(records) == len(keys) == 139
    assert keys == set(historical) | set(recent)
    assert Counter(r['original_group'] for r in records) == {'privacy': 48, 'consent': 59, 'identity': 32}
    # A citation-key year is not a publication year: use the bibliography.
    assert next(r for r in records if r['citation_key'] == '10.1109/jiot.2021.3134755')['publication_year'] == 2023
    assert next(r for r in records if r['citation_key'] == '2021-medshare')['publication_year'] == 2023
    # Avoid the lexical false positive "pre-access" as proxy re-encryption.
    assert next(r for r in records if r['citation_key'] == 'updateObodo2025MultiProviderConsent')['PRE'] == 0
    return records, matches


def aggregate(records):
    years = list(range(min(r['publication_year'] for r in records), max(r['publication_year'] for r in records)+1))
    counts = []
    for feature in [f[0] for f in FEATURES] + ['both_families']:
        for year in years:
            selected = sorted(r['citation_key'] for r in records if r['publication_year'] == year and r[feature])
            counts.append({'feature': feature, 'publication_year': year, 'count': len(selected),
                           'annual_inventory': sum(r['publication_year'] == year for r in records),
                           'citation_keys': ';'.join(selected)})
    return years, counts


def aggregate_periods(records):
    """Pool publication counts, rather than averaging annual percentages."""
    counts = []
    assert all(sum(start <= r['publication_year'] <= end for start, end in PERIODS) == 1
               for r in records)
    for feature in [f[0] for f in FEATURES] + ['both_families']:
        for start, end in PERIODS:
            inventory = [r for r in records if start <= r['publication_year'] <= end]
            selected = sorted(r['citation_key'] for r in inventory if r[feature])
            counts.append({'feature': feature, 'period_start': start, 'period_end': end,
                           'count': len(selected), 'period_inventory': len(inventory),
                           'percentage': 100 * len(selected) / len(inventory),
                           'privacy_inventory': sum(r['original_group'] == 'privacy' for r in inventory),
                           'consent_inventory': sum(r['original_group'] == 'consent' for r in inventory),
                           'identity_inventory': sum(r['original_group'] == 'identity' for r in inventory),
                           'citation_keys': ';'.join(selected)})
    return counts


def aggregate_combinations(records):
    """Keep each paper's exact profile among the twelve selected features."""
    profiles = {}
    for record in records:
        if record['both_families']:
            profile = tuple(feature for feature, *_ in FEATURES if record[feature])
            profiles.setdefault(profile, []).append(record)
    labels = {
        ('HE', 'SSI', 'CREDENTIAL', 'INDY'):
            'Homomorphic encryption + DID/SSI\n+ credentials + Indy/Aries',
        ('FL', 'DP', 'SSI'):
            'Federated learning + differential privacy\n+ DID/SSI',
        ('ZK', 'CREDENTIAL'): 'Zero-knowledge + credentials',
        ('FL', 'SSI', 'CREDENTIAL', 'INDY'):
            'Federated learning + DID/SSI\n+ credentials + Indy/Aries',
    }
    result = []
    for profile, papers in sorted(profiles.items(),
                                  key=lambda item: min(r['publication_year'] for r in item[1])):
        assert profile in labels, f'Add a readable label for the new profile: {profile}'
        for start, end in PERIODS:
            selected = sorted((r for r in papers if start <= r['publication_year'] <= end),
                              key=lambda r: (r['publication_year'], r['citation_key']))
            result.append({'features': ';'.join(profile),
                           'combination': labels[profile].replace('\n', ' '),
                           'period_start': start, 'period_end': end, 'count': len(selected),
                           'publication_years': ';'.join(str(r['publication_year']) for r in selected),
                           'citation_keys': ';'.join(r['citation_key'] for r in selected),
                           'plot_label': labels[profile]})
    assert sum(r['count'] for r in result) == sum(r['both_families'] for r in records)
    return result


def render(period_counts, preview=None):
    lookup = {(r['feature'], r['period_start']): r for r in period_counts}
    totals = [lookup[('HE', start)]['period_inventory'] for start, _ in PERIODS]
    plt.rcParams.update({'font.family': 'serif', 'font.serif': ['DejaVu Serif'],
                         'font.size': 9, 'pdf.fonttype': 42, 'ps.fonttype': 42,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'axes.edgecolor': '#8c8c8c', 'axes.linewidth': .6})
    fig = plt.figure(figsize=(7.4, 5.6))
    axes = [fig.add_axes([.085, .66, .385, .245]),
            fig.add_axes([.575, .66, .385, .245]),
            fig.add_axes([.085, .13, .48, .27])]
    groups = [FEATURES[:4], FEATURES[4:7], FEATURES[7:]]
    titles = ['(a) Encryption', '(b) Proofs and learning',
              '(c) Identity and credentials']
    # Okabe-Ito colors plus marker/line distinctions remain readable in grayscale.
    colors = ['#0072B2', '#D55E00', '#009E73', '#CC79A7', '#E69F00']
    markers = ['o', 's', '^', 'D', 'v']
    styles = ['-', '--', '-.', ':', (0, (5, 2))]
    x = np.arange(len(PERIODS))
    xlabels = [f'{start}\u2013{str(end)[2:]}\n(n = {n})'
               for (start, end), n in zip(PERIODS, totals)]
    for panel, (ax, group, title) in enumerate(zip(axes, groups, titles)):
        for i, (feature, label, _, _) in enumerate(group):
            data = [lookup[(feature, start)]['percentage'] for start, _ in PERIODS]
            if feature == 'ZK':
                label = 'Zero-knowledge proofs / credentials'
            ax.plot(x, data, color=colors[i], marker=markers[i], linestyle=styles[i],
                    linewidth=1.45, markersize=4.8, markerfacecolor='white',
                    markeredgewidth=1.1, label=label, clip_on=False)
        ax.set_title(title, loc='left', fontsize=9.3, pad=9)
        ax.set_xlim(-.08, 3.15)
        # Identity mentions have a wider range; ticks explicitly show both scales.
        ax.set_ylim(0, 35 if panel == 2 else 13)
        ax.set_yticks([0, 10, 20, 30] if panel == 2 else [0, 4, 8, 12])
        ax.yaxis.set_major_formatter(PercentFormatter(100, decimals=0))
        ax.grid(axis='y', color='#d8d8d8', linewidth=.55)
        ax.set_axisbelow(True)
        ax.set_xticks(x, xlabels, fontsize=8)
        ax.tick_params(axis='both', width=.5, length=3, labelsize=8)
        if panel < 2:
            ax.legend(loc='upper left', bbox_to_anchor=(-.02, -.30),
                      borderaxespad=0, frameon=False, fontsize=8,
                      labelspacing=.34, handlelength=2.6, handletextpad=.6)
        else:
            ax.legend(loc='upper left', bbox_to_anchor=(1.10, 1.0),
                      borderaxespad=0, frameon=False, fontsize=8,
                      labelspacing=.65, handlelength=2.6, handletextpad=.6)
    fig.text(.085, .96, 'Share of included publications naming each approach',
             fontsize=9.5)
    fig.text(.085, .025, '0% = no recorded mention; n = all included publications per window.',
             fontsize=8, linespacing=1.4)
    fig.savefig(ROOT / 'imgs' / 'technology-timeline.pdf',
                metadata={'CreationDate': None, 'ModDate': None})
    if preview:
        fig.savefig(preview, dpi=220)
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview', type=Path, help='Optional PNG preview path outside imgs/.')
    args = parser.parse_args()
    records, matches = extract()
    years, counts = aggregate(records)
    period_counts = aggregate_periods(records)
    combinations = aggregate_combinations(records)
    write_csv(REV / 'technology-timeline-records.csv', records)
    write_csv(REV / 'technology-timeline-matches.csv', matches)
    write_csv(REV / 'technology-timeline-counts.csv', counts)
    write_csv(REV / 'technology-timeline-periods.csv', period_counts)
    write_csv(REV / 'technology-timeline-combinations.csv', combinations)
    render(period_counts, args.preview)
    print('139 publication identities and bibliography years validated.')
    print('Co-reporting:', [(r['citation_key'], r['publication_year']) for r in records if r['both_families']])
    print('Generated technology-timeline.pdf and five traceable CSV files.')

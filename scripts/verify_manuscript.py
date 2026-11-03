"""Compare an external manuscript with the published source fingerprint and inventory."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys

from .build_dataset import ROOT, build_artifacts

TABLE_GROUPS = {
    'tab:privacy-works': 'privacy', 'tab:privacy-works-2': 'privacy',
    'tab:consent-works': 'consent', 'tab:consent-works-2': 'consent',
    'tab:ssi-works-part-1': 'identity', 'tab:ssi-works-part-2': 'identity',
}


def extract_membership(source):
    text = source.decode('utf-8')
    works, detailed, evaluations, fragments = [], [], {}, []
    for label, group in TABLE_GROUPS.items():
        position = text.index('\\label{' + label + '}')
        start = text.rindex(r'\begingroup', 0, position)
        end = text.index(r'\endgroup', position) + len(r'\endgroup')
        fragments.append(text[start:end])
        block = text[position:text.index(r'\end{longtable}', position)]
        for line in block.splitlines():
            if not line.startswith(r'\cite{'):
                continue
            key = re.match(r'\\cite\{([^}]+)\}', line)[1]
            works.append({'study_id': key, 'review_group': group, 'source_table': label})
            if r'\dagger' in line:
                detailed.append(key)
    for group, label in [('privacy', 'tab:privacy-evaluation'),
                         ('consent', 'tab:consent-evaluation'), ('identity', 'tab:ssi-evaluation')]:
        position = text.index('\\label{' + label + '}')
        block = text[position:text.index(r'\end{longtable}', position)]
        evaluations[group] = [re.match(r'\\cite\{([^}]+)\}', line)[1]
                              for line in block.splitlines() if line.startswith(r'\cite{')]
    questions = {m[1]: m[2] for m in re.finditer(r'\\item \\textbf\{(RQ[1-3])\}: ([^\n]+)', text)}
    objectives = {m[1]: [key.strip() for keys in re.findall(r'\\cite\w*\{([^}]+)\}', m[2])
                         for key in keys.split(',')]
                  for m in re.finditer(r'^(G[1-8]):([^\n]+)', text, re.M)}
    return {
        'manuscript_sha256': hashlib.sha256(source).hexdigest(),
        'included_works': works, 'detailed_example_ids': sorted(detailed),
        'evaluation_ids_by_group': evaluations, 'research_questions': questions,
        'objective_source_ids': objectives,
        'current_plot_files': re.findall(r'\\includegraphics(?:\[[^]]*\])?\{imgs/([^}]+\.pdf)\}', text),
    }, '\n\n'.join(fragments)


def verify(source, root=ROOT):
    actual, inventory = extract_membership(source)
    expected = json.loads((root / 'data/sources/revisao/manuscript-membership.json').read_text())
    for key, value in actual.items():
        if expected[key] != value:
            raise ValueError('External manuscript differs from the public snapshot: ' + key)
    excerpt = (root / 'data/sources/revisao/manuscript-inventory.tex').read_text()
    excerpt = '\n'.join(line for line in excerpt.splitlines() if not line.startswith('%')).strip()
    if inventory.strip() != excerpt:
        raise ValueError('External manuscript inventory descriptions differ from the published excerpt')
    return actual


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manuscript', type=Path)
    args = parser.parse_args(argv)
    try:
        build_artifacts()
        result = verify(args.manuscript.read_bytes())
    except (ValueError, KeyError, OSError) as exc:
        print(f'Manuscript verification failed: {exc}', file=sys.stderr)
        return 1
    print(json.dumps({'status': 'matched', 'included_works': len(result['included_works']),
                      'detailed_examples': len(result['detailed_example_ids']),
                      'manuscript_sha256': result['manuscript_sha256']}))
    return 0

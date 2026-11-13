"""Plot reported component costs and encrypted-learning tradeoffs with Matplotlib.

Run: python revisao/plot_processing_costs.py
Requires matplotlib. Reads processing-costs-data.json, checks source membership,
and writes a vector PDF and a 300-dpi PNG. No image-generation model is used.
"""
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

REV = Path(__file__).resolve().parent
ROOT = REV.parent


def load_data():
    data = json.loads((REV / 'processing-costs-data.json').read_text())
    with (REV / 'synthesis-evidence-matrix.csv').open() as f:
        sources = {r['matrix_id']: r for r in csv.DictReader(f)}
    for name in ('privda', 'kang'):
        row = data[name]
        source = sources[row['matrix_id']]
        assert row['citation_key'] == source['citation_key']
        assert source['verification_status'] == 'primary_fulltext_verified'
    for low, high in data['privda']['ranges_ms'].values():
        assert 0 <= low <= high
    for row in data['kang']['measurements']:
        assert row['training_minutes'] > 0
        assert 0 <= row['accuracy'] <= 1 and 0 <= row['auc'] <= 1
    return data


def draw(data):
    plt.rcParams.update({
        'font.family': 'serif', 'font.serif': ['DejaVu Serif'], 'font.size': 9,
        'axes.titlesize': 10, 'axes.labelsize': 9, 'xtick.labelsize': 8,
        'ytick.labelsize': 9, 'pdf.fonttype': 42, 'ps.fonttype': 42,
        'axes.spines.top': False, 'axes.spines.right': False,
        'axes.spines.left': False, 'axes.axisbelow': True,
    })
    blue, orange = '#0072B2', '#D55E00'
    fig, axes = plt.subplots(1, 3, figsize=(7.3, 3.25),
                             gridspec_kw={'width_ratios': [1.15, .9, 1]})
    fig.subplots_adjust(left=.07, right=.98, top=.76, bottom=.25, wspace=.42)
    a, b, c = axes
    a.set_title('(a) PrivDA: aggregation', loc='left', pad=36)
    a.text(0, 1.13, '5–50 producers', transform=a.transAxes, fontsize=8)
    for y, (label, limits) in enumerate(data['privda']['ranges_ms'].items()):
        lo, hi = limits
        a.plot([lo, hi], [y, y], color=blue, linewidth=2.3, marker='|', markersize=9)
        a.text(lo, y+.12, label, fontsize=8, va='bottom')
        a.text((lo+hi)/2, y-.12, f'{lo}–{hi} ms', fontsize=8, ha='center', va='top')
    a.set(xlim=(0, 460), ylim=(-.5, 1.7), xlabel='Time (ms)', yticks=[], xticks=[0, 200, 400])
    a.grid(axis='x', color='.9', linewidth=.6)
    b.set_title('(b) Kang: training', loc='left', pad=36)
    b.text(0, 1.13, 'METABRIC logistic regression', transform=b.transAxes, fontsize=8)
    rows = data['kang']['measurements']
    for y, (row, color) in enumerate(zip(rows, [blue, orange])):
        value = row['training_minutes']
        b.barh(y, value, height=.32, color=color)
        b.text(0, y+.23, row['method'], fontsize=8, va='bottom')
        b.text(value+3, y, str(value), fontsize=9, va='center')
    b.set(xlim=(0, 125), ylim=(-.5, 1.7), xlabel='Training time (min)', yticks=[], xticks=[0, 50, 100])
    b.grid(axis='x', color='.9', linewidth=.6)
    c.set_title('(c) Kang: prediction', loc='left', pad=36)
    c.text(0, 1.13, '5-fold cross-validation', transform=c.transAxes, fontsize=8)
    for y, metric in enumerate(['accuracy', 'auc']):
        values = [r[metric] for r in rows]
        c.plot(values, [y, y], color='.5', linewidth=1)
        c.scatter(values[0], y, color=blue, marker='o', s=30, zorder=3)
        c.scatter(values[1], y, color=orange, marker='s', s=28, zorder=3)
        c.text(.695, y+.19, metric.upper() if metric == 'auc' else 'Accuracy', fontsize=8)
        c.text(values[0], y+.08, f'{values[0]:.3f}', ha='center', va='bottom', fontsize=8)
        c.text(values[1], y-.10, f'{values[1]:.3f}', ha='center', va='top', fontsize=8)
    c.set(xlim=(.695, .775), ylim=(-.5, 1.7), xlabel='Score (detail scale)', yticks=[], xticks=[.70, .73, .76])
    c.grid(axis='x', color='.9', linewidth=.6)
    handles = [Line2D([], [], linestyle='', marker='o', color=blue, label='Plaintext'),
               Line2D([], [], linestyle='', marker='s', color=orange, label='Encrypted')]
    c.legend(handles=handles, loc='upper center', bbox_to_anchor=(.48, -.34),
             ncol=2, frameon=False, fontsize=8, columnspacing=1, handletextpad=.3)
    for ax in axes:
        ax.tick_params(axis='y', length=0)
    for extension in ['pdf', 'png']:
        options = {'metadata': {'CreationDate': None, 'ModDate': None}} if extension == 'pdf' else {'dpi': 300}
        fig.savefig(ROOT / 'imgs' / f'synthesis-processing-costs.{extension}', **options)
    plt.close(fig)
    print('Generated synthesis-processing-costs.pdf and .png from primary-source values.')
    print('Training-time ratio:', rows[1]['training_minutes'] / rows[0]['training_minutes'])


if __name__ == '__main__':
    draw(load_data())

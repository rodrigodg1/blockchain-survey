"""Run the manuscript's unchanged plotting scripts in an isolated working directory.

Validate the dataset first, compare every regenerated timeline table with the
published records, then write the two current figures and their PNG previews.
"""
from importlib.metadata import version
from pathlib import Path
import argparse
import csv
import io
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile

from .build_dataset import ROOT, build_artifacts, check_artifacts, digest, json_bytes

TRACE_FILES = ['technology-timeline-' + part + '.csv'
               for part in ('records', 'matches', 'counts', 'periods', 'combinations')]
PLOT_INPUTS = [
    'references-revised.bib', 'historical-extraction.csv',
    'revisao/recent-extraction.csv', 'revisao/synthesis-evidence-matrix.csv',
    'revisao/manuscript-inventory.tex', 'revisao/processing-costs-data.json',
    'revisao/plot_technology_timeline.py', 'revisao/plot_processing_costs.py',
]


def render_plots(root=ROOT):
    """Preserve both plotters' existing input layout without an external manuscript."""
    source = root / 'data/sources'
    with tempfile.TemporaryDirectory(prefix='survey-plots-') as temporary:
        stage = Path(temporary)
        (stage / 'imgs').mkdir()
        for name in PLOT_INPUTS:
            destination = stage / ('main.tex' if name.endswith('manuscript-inventory.tex') else name)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / name, destination)
        env = dict(os.environ, MPLCONFIGDIR=str(stage / 'matplotlib-cache'))
        subprocess.run([sys.executable, str(stage / 'revisao/plot_technology_timeline.py'),
                        '--preview', str(stage / 'imgs/technology-timeline.png')],
                       cwd=stage, env=env, check=True)
        subprocess.run([sys.executable, str(stage / 'revisao/plot_processing_costs.py')],
                       cwd=stage, env=env, check=True)
        traces = {name: (stage / 'revisao' / name).read_bytes() for name in TRACE_FILES}
        figures = {name: (stage / 'imgs' / name).read_bytes() for name in (
            'technology-timeline.pdf', 'technology-timeline.png',
            'synthesis-processing-costs.pdf', 'synthesis-processing-costs.png')}
    return figures, traces


def verify_trace_tables(root, traces):
    for name, payload in traces.items():
        expected = list(csv.DictReader((root / 'data/sources/revisao' / name).open(newline='')))
        actual = list(csv.DictReader(io.StringIO(payload.decode())))
        if actual != expected:
            raise ValueError('Regenerated timeline records differ from the published source: ' + name)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Regenerate and compare without writing outputs')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'data/figures')
    args = parser.parse_args(argv)
    try:
        artifacts = build_artifacts()
        check_artifacts(ROOT, artifacts)
        figures, traces = render_plots()
        verify_trace_tables(ROOT, traces)
        snapshot = json.loads((ROOT / 'data/source-snapshot.json').read_text())
        manifest = {
            'snapshot_date': snapshot['artifact_date'],
            'manuscript_sha256': snapshot['manuscript_sha256'],
            'dataset_sha256': digest(artifacts['survey-dataset.csv']),
            'generator': 'scripts/reproduce_plots.py',
            'python': platform.python_version(),
            'packages': {name: version(name) for name in ('matplotlib', 'numpy', 'fonttools', 'pillow')},
            'inputs': {name: digest((ROOT / 'data/sources' / name).read_bytes()) for name in PLOT_INPUTS},
            'outputs': {name: digest(payload) for name, payload in figures.items()},
            'scope': 'Replots retained literature measurements and descriptive counts; no new experiments',
        }
        figures['manifest.json'] = json_bytes(manifest)
        output = args.output_dir.resolve()
        if args.check:
            for name, payload in figures.items():
                if not (output / name).is_file() or (output / name).read_bytes() != payload:
                    raise ValueError('Missing or changed plot output: ' + name)
        else:
            output.mkdir(parents=True, exist_ok=True)
            for name, payload in figures.items():
                (output / name).write_bytes(payload)
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as exc:
        print(f'Plot reproduction failed: {exc}', file=sys.stderr)
        return 1
    print(json.dumps({'status': 'validated' if args.check else 'reproduced',
                      'figures': 2, 'trace_tables': len(traces), 'output': str(output)}))
    return 0

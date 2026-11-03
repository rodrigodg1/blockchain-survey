"""Run the manuscript's unchanged plotting scripts in an isolated working directory.

Validate the dataset first, compare every regenerated timeline table with the
published records, then write the current chronology figure and its PNG preview.
The excluded two-study illustration is available only with --include-legacy.
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
    'revisao/manuscript-inventory.tex', 'revisao/plot_technology_timeline.py',
]
LEGACY_INPUTS = ['revisao/processing-costs-data.json', 'revisao/plot_processing_costs.py']


def render_plots(root=ROOT, include_legacy=False):
    """Preserve the original plotters and stage only the requested outputs."""
    source = root / 'data/sources'
    with tempfile.TemporaryDirectory(prefix='survey-plots-') as temporary:
        stage = Path(temporary)
        (stage / 'imgs').mkdir()
        for name in PLOT_INPUTS + (LEGACY_INPUTS if include_legacy else []):
            destination = stage / ('main.tex' if name.endswith('manuscript-inventory.tex') else name)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / name, destination)
        env = dict(os.environ, MPLCONFIGDIR=str(stage / 'matplotlib-cache'))
        subprocess.run([sys.executable, str(stage / 'revisao/plot_technology_timeline.py'),
                        '--preview', str(stage / 'imgs/technology-timeline.png')],
                       cwd=stage, env=env, check=True)
        if include_legacy:
            subprocess.run([sys.executable, str(stage / 'revisao/plot_processing_costs.py')],
                           cwd=stage, env=env, check=True)
        traces = {name: (stage / 'revisao' / name).read_bytes() for name in TRACE_FILES}
        names = ['technology-timeline.pdf', 'technology-timeline.png']
        if include_legacy:
            names += ['synthesis-processing-costs.pdf', 'synthesis-processing-costs.png']
        figures = {name: (stage / 'imgs' / name).read_bytes() for name in names}
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
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--include-legacy', action='store_true',
                        help='Also render the excluded two-study illustration in a separate output directory')
    args = parser.parse_args(argv)
    if args.include_legacy and (args.output_dir is None or args.output_dir.resolve() == (ROOT / 'data/figures').resolve()):
        parser.error('--include-legacy requires a separate --output-dir')
    try:
        artifacts = build_artifacts()
        check_artifacts(ROOT, artifacts)
        figures, traces = render_plots(include_legacy=args.include_legacy)
        verify_trace_tables(ROOT, traces)
        snapshot = json.loads((ROOT / 'data/source-snapshot.json').read_text())
        manifest = {
            'snapshot_date': snapshot['artifact_date'],
            'manuscript_sha256': snapshot['manuscript_sha256'],
            'dataset_sha256': digest(artifacts['survey-dataset.csv']),
            'generator': 'scripts/reproduce_plots.py',
            'python': platform.python_version(),
            'packages': {name: version(name) for name in ('matplotlib', 'numpy', 'fonttools', 'pillow')},
            'current_plot_files': snapshot['current_plot_files'],
            'excluded_plot_files_generated': snapshot['excluded_plot_files'] if args.include_legacy else [],
            'inputs': {name: digest((ROOT / 'data/sources' / name).read_bytes())
                       for name in PLOT_INPUTS + (LEGACY_INPUTS if args.include_legacy else [])},
            'outputs': {name: digest(payload) for name, payload in figures.items()},
            'scope': 'Current plot describes the 139-publication inventory; optional legacy illustration is excluded from the manuscript',
        }
        figures['manifest.json'] = json_bytes(manifest)
        output = (args.output_dir or ROOT / 'data/figures').resolve()
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
                      'figures': sum(name.endswith('.pdf') for name in figures),
                      'legacy_included': args.include_legacy,
                      'trace_tables': len(traces), 'output': str(output)}))
    return 0

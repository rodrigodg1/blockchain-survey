"""Regenerate the chronology from retained descriptions in an isolated directory.

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

from .build_dataset import ROOT, build_artifacts, validate_artifacts, digest, json_bytes

TRACE_FILES = ['technology-timeline-' + part + '.csv'
               for part in ('records', 'matches', 'counts', 'periods', 'combinations')]
PLOT_INPUTS = [
    'references-revised.bib', 'historical-extraction.csv',
    'revisao/recent-extraction.csv', 'revisao/synthesis-evidence-matrix.csv',
    'revisao/application-inventory.tex', 'revisao/plot_technology_timeline.py',
]
LEGACY_INPUTS = ['revisao/processing-costs-data.json', 'revisao/plot_processing_costs.py']


def render_plots(root=ROOT, include_legacy=False):
    """Preserve the original plotters and stage only the requested outputs."""
    source = root / 'data/sources'
    with tempfile.TemporaryDirectory(prefix='survey-plots-') as temporary:
        stage = Path(temporary)
        (stage / 'imgs').mkdir()
        (stage / 'cache').mkdir()
        for name in PLOT_INPUTS + (LEGACY_INPUTS if include_legacy else []):
            destination = stage / ('main.tex' if name.endswith('application-inventory.tex') else name)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / name, destination)
        env = dict(os.environ, MPLCONFIGDIR=str(stage / 'matplotlib-cache'),
                   XDG_CACHE_HOME=str(stage / 'cache'), MPLBACKEND='Agg', PYTHONUTF8='1')
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
        with (root / 'data/sources/revisao' / name).open(newline='', encoding='utf-8') as stream:
            expected = list(csv.DictReader(stream))
        actual = list(csv.DictReader(io.StringIO(payload.decode())))
        if actual != expected:
            raise ValueError('Regenerated timeline records differ from the published source: ' + name)


def validate_figure_outputs(output, figures, manifest):
    """Verify retained bytes, inputs, and renderer-dependent reproduction separately."""
    retained = json.loads((output / 'manifest.json').read_text(encoding='utf-8'))
    rendering_fields = {'python', 'packages', 'platform', 'outputs'}
    for key, value in manifest.items():
        if key not in rendering_fields and retained.get(key) != value:
            raise ValueError('Figure provenance differs from current inputs: ' + key)
    if set(retained['outputs']) != set(manifest['outputs']):
        raise ValueError('Figure output inventory differs')
    for name, expected in retained['outputs'].items():
        path = output / name
        if not path.is_file() or digest(path.read_bytes()) != expected:
            raise ValueError('Missing or altered retained figure: ' + name)
    identical = all(retained['outputs'][name] == digest(figures[name])
                    for name in manifest['outputs'])
    same_environment = all(retained.get(key) == manifest.get(key)
                           for key in ('python', 'packages', 'platform'))
    if same_environment and not identical:
        raise ValueError('Rendering changed in the recorded environment')
    return 'identical' if identical else 'different_rendering_environment'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--validate', action='store_true', help='Regenerate and compare without writing outputs')
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--include-legacy', action='store_true',
                        help='Also render the excluded two-study illustration in a separate output directory')
    parser.add_argument('--check', dest='validate', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.include_legacy and (args.output_dir is None or args.output_dir.resolve() == (ROOT / 'data/figures').resolve()):
        parser.error('--include-legacy requires a separate --output-dir')
    try:
        artifacts = build_artifacts()
        validate_artifacts(ROOT, artifacts)
        figures, traces = render_plots(include_legacy=args.include_legacy)
        verify_trace_tables(ROOT, traces)
        snapshot = json.loads((ROOT / 'data/source-snapshot.json').read_text())
        manifest = {
            'snapshot_date': snapshot['artifact_date'],
            'reference_source_sha256': snapshot['reference_source_sha256'],
            'dataset_sha256': digest(artifacts['survey-dataset.csv']),
            'generator': 'scripts/reproduce_plots.py',
            'python': platform.python_version(),
            'platform': {'system': platform.system(), 'machine': platform.machine()},
            'packages': {name: version(name) for name in ('matplotlib', 'numpy', 'fonttools', 'pillow')},
            'current_plot_files': snapshot['current_plot_files'],
            'excluded_plot_files_generated': snapshot['excluded_plot_files'] if args.include_legacy else [],
            'inputs': {name: digest((ROOT / 'data/sources' / name).read_bytes())
                       for name in PLOT_INPUTS + (LEGACY_INPUTS if args.include_legacy else [])},
            'outputs': {name: digest(payload) for name, payload in figures.items()},
            'scope': 'Chronology describes the 139-publication inventory; the optional legacy illustration describes two studies only',
        }
        output = (args.output_dir or ROOT / 'data/figures').resolve()
        if args.validate:
            rendering = validate_figure_outputs(output, figures, manifest)
        else:
            rendering = 'generated'
            figures['manifest.json'] = json_bytes(manifest)
            output.mkdir(parents=True, exist_ok=True)
            for name, payload in figures.items():
                (output / name).write_bytes(payload)
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as exc:
        print(f'Plot reproduction failed: {exc}', file=sys.stderr)
        return 1
    print(json.dumps({'status': 'validated' if args.validate else 'reproduced',
                      'figures': sum(name.endswith('.pdf') for name in figures),
                      'legacy_included': args.include_legacy,
                      'trace_tables': len(traces), 'numerical_records': 'identical',
                      'rendering': rendering, 'output': str(output)}))
    return 0

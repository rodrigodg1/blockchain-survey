"""Validate the retained collection, optionally comparing an external LaTeX source."""
from pathlib import Path
import argparse
import json
import sys

from .build_dataset import ROOT, build_artifacts, validate_artifacts
from .source_tables import extract_membership, platform_records


def verify(source, root=ROOT, external=True):
    expected = json.loads((root / 'data/sources/revisao/collection-membership.json').read_text(encoding='utf-8'))
    actual, inventory, _ = extract_membership(source, expected['evaluation_ids_by_group'])
    for key, value in actual.items():
        if key == 'reference_source_sha256' and not external:
            continue
        if expected[key] != value:
            raise ValueError('Source differs from the retained collection: ' + key)
    excerpt = (root / 'data/sources/revisao/application-inventory.tex').read_text(encoding='utf-8').strip()
    if inventory.strip() != excerpt:
        raise ValueError('Source application descriptions differ from the retained inventory')
    comparisons = (root / 'data/sources/revisao/comparison-excerpts.tex').read_text(encoding='utf-8')
    if platform_records(source.decode('utf-8')) != platform_records(comparisons):
        raise ValueError('Source platform descriptions differ from the retained comparisons')
    return actual


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', nargs='?', type=Path, help='Optional external LaTeX source')
    args = parser.parse_args(argv)
    try:
        artifacts = build_artifacts()
        validate_artifacts(ROOT, artifacts)
        if args.source:
            source = args.source.read_bytes()
        else:
            source = b'\n\n'.join((ROOT / 'data/sources/revisao' / name).read_bytes()
                                  for name in ('application-inventory.tex', 'comparison-excerpts.tex'))
        result = verify(source, external=bool(args.source))
    except (ValueError, KeyError, OSError) as exc:
        print(f'Source validation failed: {exc}', file=sys.stderr)
        return 1
    print(json.dumps({'status': 'matched', 'included_works': len(result['included_works']),
                      'external_source_compared': bool(args.source),
                      'evaluation_formats': result['evaluation_locations']}))
    return 0

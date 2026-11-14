"""Validate the retained collection, optionally comparing an external LaTeX source."""
from pathlib import Path
import argparse
import json
import sys

from .build_dataset import ROOT, build_artifacts, validate_artifacts
from .source_tables import (extract_membership, platform_records, section_fragment,
                            survey_method_fragment, table_fragment, without_comments)


def verify(source, root=ROOT, external=True):
    expected = json.loads((root / 'data/sources/revisao/collection-membership.json').read_text(encoding='utf-8'))
    actual, inventory, _ = extract_membership(source, expected['evaluation_ids_by_group'])
    for key, value in actual.items():
        if key == 'reference_source_sha256' and not external:
            continue
        if expected[key] != value:
            raise ValueError('Source differs from the retained collection: ' + key)
    text = without_comments(source.decode('utf-8'))
    excerpt = without_comments((root / 'data/sources/revisao/application-inventory.tex')
                               .read_text(encoding='utf-8')).strip()
    if inventory.strip() != excerpt:
        raise ValueError('Source application descriptions differ from the retained inventory')
    comparisons = without_comments((root / 'data/sources/revisao/comparison-excerpts.tex')
                                   .read_text(encoding='utf-8'))
    method = (root / 'data/sources/revisao/survey-method.tex').read_text(encoding='utf-8')
    if survey_method_fragment(text) != survey_method_fragment(method):
        raise ValueError('Source Survey Method differs from the retained method')
    if section_fragment(text, 'sec:privacy-evaluation') != section_fragment(comparisons, 'sec:privacy-evaluation'):
        raise ValueError('Source privacy synthesis differs from the retained comparison')
    for label in ('tab:consent-evaluation', 'tab:ssi-evaluation',
                  'tab:worked-control-comparisons', 'tab:architecture-requirements'):
        if table_fragment(text, label) != table_fragment(comparisons, label):
            raise ValueError('Source comparison differs from the retained excerpt: ' + label)
    platform_reference = comparisons
    if external:
        platform_reference = (root / 'data/sources/revisao/reference-platforms.tex').read_text(
            encoding='utf-8')
    if platform_records(text) != platform_records(platform_reference):
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
                                  for name in ('application-inventory.tex', 'comparison-excerpts.tex',
                                               'survey-method.tex'))
        result = verify(source, external=bool(args.source))
    except (ValueError, KeyError, OSError) as exc:
        print(f'Source validation failed: {exc}', file=sys.stderr)
        return 1
    print(json.dumps({'status': 'matched', 'included_works': len(result['included_works']),
                      'external_source_compared': bool(args.source),
                      'evaluation_formats': result['evaluation_locations']}))
    return 0

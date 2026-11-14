"""Read retained LaTeX tables and synthesis passages without executing LaTeX."""
import hashlib
from pathlib import PurePosixPath
import re

TABLE_GROUPS = {
    'tab:privacy-works': 'privacy', 'tab:privacy-works-2': 'privacy',
    'tab:consent-works': 'consent', 'tab:consent-works-2': 'consent',
    'tab:ssi-works-part-1': 'identity', 'tab:ssi-works-part-2': 'identity',
}
PLATFORM_TABLES = {
    'tab:privacy-platforms': ('privacy', ('system', 'protected_information',
                                        'mechanism_and_trust', 'code_and_status')),
    'tab:ssi-platforms': ('identity', ('component', 'role', 'ledger_dependency',
                                    'capabilities_and_limits')),
}


def without_comments(text):
    return re.sub(r'(?<!\\)%[^\n]*', '', text)


def citation_ids(text):
    return list(dict.fromkeys(key.strip() for match in re.finditer(
        r'\\cite(?:t|p|alp|author|year)?\*?(?:\[[^\]]*\])*\{([^{}]+)\}', text)
        for key in match[1].split(',') if key.strip()))


def table_fragment(text, label):
    for match in re.finditer(r'\\begin\{(longtable|table\*?)\}.*?\\end\{\1\}', text, re.S):
        if r'\label{' + label + '}' in match[0]:
            return match[0]
    raise ValueError('Missing source table: ' + label)


def table_rows(fragment):
    delimiters = [r'\endlastfoot', r'\endhead'] if r'\begin{longtable}' in fragment else [r'\midrule']
    positions = [fragment.index(marker) + len(marker) for marker in delimiters if marker in fragment]
    if not positions:
        raise ValueError('Missing table body delimiter')
    body = fragment[max(positions):]
    result = []
    for row in re.split(r'\\\\(?:\[[^\]]*\])?', body):
        row = re.sub(r'\\addlinespace(?:\[[^\]]*\])?', '', row).strip()
        cells = re.split(r'(?<!\\)&', row)
        if len(cells) > 1:
            result.append([cell.strip() for cell in cells])
    return result


def section_fragment(text, label):
    marker = r'\label{' + label + '}'
    if marker not in text:
        raise ValueError('Missing synthesis passage: ' + label)
    start = text.index(marker)
    following = re.search(r'\\(?:sub)*section\*?\{', text[start + len(marker):])
    end = start + len(marker) + following.start() if following else len(text)
    return text[start:end].strip()


def survey_method_fragment(text):
    text = without_comments(text)
    heading = re.search(r'\\section\{Survey Method\}', text)
    if not heading:
        raise ValueError('Missing Survey Method section')
    following = re.search(r'\\section\*?\{', text[heading.end():])
    end = heading.end() + following.start() if following else len(text)
    return text[heading.start():end].strip()


def objective_sources(text):
    objectives = {}
    if r'\label{tab:architecture-requirements}' in text:
        rows = table_rows(table_fragment(text, 'tab:architecture-requirements'))
        entries = []
        for cells in rows:
            match = re.match(r'(?:\\textbf\{\s*)?(G[1-8])\s*:', cells[0])
            if not match or len(cells) != 3:
                raise ValueError('Invalid evaluation objective row')
            entries.append((match[1], ' '.join(cells)))
    else:
        # Retained historical excerpts used one bare G-label per line.
        entries = re.findall(r'^(G[1-8]):([^\n]+)', text, re.M)
    for key, passage in entries:
        if key in objectives:
            raise ValueError('Duplicate evaluation objective: ' + key)
        objectives[key] = citation_ids(passage)
    if set(objectives) != {f'G{i}' for i in range(1, 9)}:
        raise ValueError('Expected eight evaluation objectives')
    return objectives


def extract_membership(source, evaluation_candidates=None):
    text = without_comments(source.decode('utf-8'))
    works, fragments, summaries = [], [], []
    for label, group in TABLE_GROUPS.items():
        block = table_fragment(text, label)
        fragments.append(block)
        for cells in table_rows(block):
            match = re.match(r'\\cite\{([^}]+)\}', cells[0])
            if not match or len(cells) != 3:
                raise ValueError('Invalid application row in ' + label)
            key = match[1]
            works.append({'study_id': key, 'review_group': group, 'source_table': label})
            summaries.append({'study_id': key, 'application': cells[1], 'approach': cells[2]})
    by_id = {row['study_id']: row['review_group'] for row in works}
    if len(by_id) != len(works):
        raise ValueError('Duplicate application identity in source tables')
    evaluations, locations = {}, {}
    for group in ('privacy', 'consent', 'identity'):
        label = 'tab:ssi-evaluation' if group == 'identity' else 'tab:' + group + '-evaluation'
        if r'\label{' + label + '}' in text:
            evaluations[group] = [citation_ids(row[0])[0]
                                  for row in table_rows(table_fragment(text, label))]
            locations[group] = {'format': 'table', 'label': label}
        elif group == 'privacy':
            label = 'sec:privacy-evaluation'
            passage = section_fragment(text, label)
            if evaluation_candidates is None:
                raise ValueError('Prose evaluation membership requires extraction identities')
            candidates = set(evaluation_candidates[group])
            # Older comparisons and contextual citations remain outside this
            # explicitly recorded evaluation subset.
            evaluations[group] = [key for key in citation_ids(passage)
                                  if by_id.get(key) == group and key in candidates]
            if not evaluations[group]:
                raise ValueError('Synthesis passage contains no recorded evaluation identities')
            locations[group] = {'format': 'prose', 'label': label}
        else:
            raise ValueError('Missing evaluation source for ' + group)
    questions = dict(re.findall(r'\\item\s+\\textbf\{(RQ[1-3])\}:\s*([^\n]+)', text))
    inline_questions = re.findall(r'\((RQ[1-3])\)\s*([^?\n]+\?)', text)
    for key, question in inline_questions:
        if key in questions and questions[key] != question:
            raise ValueError('Conflicting research question: ' + key)
        questions[key] = question
    if set(questions) != {'RQ1', 'RQ2', 'RQ3'}:
        raise ValueError('Expected three research questions')
    objectives = objective_sources(text)
    return {
        'reference_source_sha256': hashlib.sha256(source).hexdigest(),
        'included_works': works, 'presented_evaluation_ids_by_group': evaluations,
        'evaluation_locations': locations, 'research_questions': questions,
        'objective_source_ids': objectives,
        'current_plot_files': [PurePosixPath(path).name for path in re.findall(
            r'\\includegraphics(?:\[[^]]*\])?\{([^}]+\.pdf)\}', text)],
    }, '\n\n'.join(fragments), summaries


def plain_text(value):
    value = re.sub(r'\\href\{([^{}]+)\}\{([^{}]+)\}', r'\2 (\1)', value)
    value = re.sub(r'\\cite\w*\*?(?:\[[^\]]*\])*\{[^{}]+\}', '', value)
    value = re.sub(r'\\(?:texttt|textbf|emph|url)\{([^{}]*)\}', r'\1', value)
    value = value.replace('~', ' ').replace(r'\%', '%').replace(r'\&', '&')
    return re.sub(r'\s+', ' ', value).strip().replace(' .', '.')


def platform_records(text):
    result = {}
    for label, (group, columns) in PLATFORM_TABLES.items():
        rows = []
        for cells in table_rows(table_fragment(without_comments(text), label)):
            if len(cells) != len(columns):
                raise ValueError('Invalid platform column count: ' + label)
            row = dict(zip(columns, map(plain_text, cells)))
            row['reference_ids'] = citation_ids(' '.join(cells))
            row['direct_urls'] = re.findall(r'\\(?:href|url)\{([^{}]+)\}', ' '.join(cells))
            rows.append(row)
        result[group] = rows
    return result

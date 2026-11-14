# Maintain the retained collection

The collection contains 139 included publications, all contributing to the classification of applications and mechanisms. Its qualitative synthesis compares selected multi-stakeholder data-sharing operations; preserve that distinction when updating evidence, counts, and documentation.

## Rebuild unchanged inputs

Run the commands in [REPRODUCE.md](../REPRODUCE.md). Rebuilding unchanged inputs must leave the eight generated data files unchanged. Validate numerical traces and retained figure fingerprints before publishing.

## Update evidence or descriptions

1. Review each changed source. Preserve citation keys, query identifiers, examined versions, and evidence limits for included publications.
2. Update the application inventory and comparison excerpts under `data/sources/revisao/`. Preserve the six inventory labels and the source text. Record whether evaluation identities appear in a table or in prose. Extraction membership and presentation membership must remain separate. Neither establishes uniform analytical coverage of all included publications; retain source-specific gaps and limits.
3. Reconcile `collection-membership.json` with the inventory, synthesis matrix, evaluation records, research questions, and objective citations. Contextual sources remain outside application counts.
4. Update source-table pointers when inventory partitions change. A changed pointer does not change the study's group or its extracted findings.
5. Update the bibliography only from verified source information. Keep publication years separate from access dates. Record the source for changes to included publication metadata.
6. Update `data/source-snapshot.json` deliberately: snapshot date, source fingerprints, expected counts, and the generated dataset fingerprint. Investigate every changed input before accepting its new hash. Source text uses LF newlines.
7. Regenerate data and figures, execute the tests, compare every numerical trace, and inspect the figures. A new output hash alone does not establish numerical or scientific correctness.
8. Review the documentation and local links. Publish only after all documented reproduction commands succeed. Confirm the result from a fresh clone and compare the local and remote commit identifiers.

When an external LaTeX source is available, compare it with the retained reference:

```sh
python3 verify_source.py /path/to/source.tex
```

This optional command reads the external file without modifying it. It compares the full source fingerprint, survey method, inventory identities and descriptions, evaluation presentation, research questions, objective citations, and the reference platform-table form. Editorial changes can change the full fingerprint without changing numerical results; reconcile them explicitly.

Refresh `data/sources/revisao/survey-method.tex` and `reference-platforms.tex` when their corresponding source passages change. The platform entries in `comparison-excerpts.tex` retain the repository's specific supporting citations and direct documentation or release links. Preserve that evidence when the manuscript uses consolidated platform references; check substantive agreement without replacing the more specific repository sources with generic links. Retain source-specific versions and access dates without implying a new verification.

The default `python3 verify_source.py` uses only retained repository inputs. It cannot detect later changes to an external source that is not supplied.

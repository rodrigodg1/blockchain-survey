# Maintain the retained collection

The current snapshot contains 139 included publications (48/59/32), 53 detailed application comparisons, 17 contextual sources, 41 evaluation extraction records, and comparisons of 19 privacy systems and six identity components. Original Scholar observations, additional exports, and the targeted follow-up retain separate provenance.

## Rebuild unchanged inputs

Run the commands in [REPRODUCE.md](../REPRODUCE.md). Rebuilding unchanged inputs must leave the nine generated data files unchanged. Validate numerical traces and retained figure fingerprints before publishing. Historical retrieval CSVs must retain their recorded hashes.

## Update evidence or descriptions

1. Review each changed source. Preserve citation keys, retrieval identifiers, versions, access limitations, and pending decisions. Retrieval alone does not establish eligibility.
2. Update the application inventory and comparison excerpts under `data/sources/revisao/`. Preserve the six inventory labels and the source text. Record whether evaluation identities appear in a table or in prose. Extraction membership and presentation membership must remain separate.
3. Reconcile `collection-membership.json` with the inventory, synthesis matrix, evaluation records, research questions, and objective citations. Contextual sources remain outside application counts.
4. Update source-table pointers when inventory partitions change. A changed pointer does not change the study's group or its extracted findings. Do not replace historical extraction with newly inferred information.
5. Update the bibliography only from verified source information. Keep publication years separate from access dates. Preserve retrieval and assessment records unless new evidence explicitly revises them.
6. Update `data/source-snapshot.json` deliberately: snapshot date, source fingerprints, expected counts, and the generated dataset fingerprint. Investigate every changed input before accepting its new hash. Source text uses LF newlines.
7. Regenerate data and figures, execute the tests, compare every numerical trace, and inspect the figures. A new output hash alone does not establish numerical or scientific correctness.
8. Review the documentation and local links. Publish only after all documented reproduction commands succeed. Confirm the result from a fresh clone and compare the local and remote commit identifiers.

When an external LaTeX source is available, compare it with the retained reference:

```sh
python3 verify_source.py /path/to/source.tex
```

This optional command reads the external file without modifying it. It compares the full source fingerprint, inventory identities and descriptions, evaluation presentation, research questions, objective citations, and platform descriptions. Editorial changes can change the full fingerprint without changing numerical results; reconcile them explicitly.

The default `python3 verify_source.py` uses only retained repository inputs. It cannot detect later changes to an external source that is not supplied.

## Historical records

Dated assessment notes and earlier snapshots preserve their original context. Earlier totals describe those dates. Current totals come from `data/counts.json`; current plot records come from the five `technology-timeline-*.csv` files. The old processing-cost illustration is optional and always uses a separate output directory.

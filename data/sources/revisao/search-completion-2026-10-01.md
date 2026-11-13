# Search completion and screening record

## Scope and decision rules

This follow-up executes the previously uncompleted database queries and extends Google Scholar pagination. Searches are executed on 1 October 2026. The publication window remains 1 January 2024 to 30 September 2026. Year-only database filters are followed by publication-date verification. Search estimates are not treated as exact record counts.

The nine title predicates in the manuscript are retained. Equivalent Boolean expressions in an article-title field are recorded with the expression actually submitted. Database stemming can retrieve additional titles. Such records receive a separate title-eligibility check. No citation-count, author-prestige, or journal-ranking filter is applied.

Each observation retains its database, query, result position or exported identifier, retrieval date, title, URL, and metadata. DOI matching applies only to nonempty normalized DOIs. Missing DOIs are compared using normalized titles and then verified against the primary publication. Versions and homonymous titles are not silently merged.

Reviews support positioning but are not application records. Application eligibility requires a blockchain-assisted personal-data sharing, permission, or identity workflow and an accessible method-bearing primary text. Missing full text remains pending. An abstract, index entry, conference programme, or publisher access badge does not establish an implementation or security guarantee. Retracted sources are checked against the primary retraction notice before a final disposition.

The 18 previously unresolved observations are assessed separately from newly retrieved candidates. Original search observations and prior decisions remain recoverable. This follow-up cannot reconstruct the undocumented screening decisions underlying the original collection. No independent human screening, inter-rater agreement, or exhaustive literature coverage is claimed.

## Retrieval and assessment checkpoint

Scopus recognized USP institutional access. Article-title queries S02/S05/S08 returned **496/47/175 observations**. All result records were exported with citation metadata, identifiers, abstracts, and keywords in the three `search-expansion-S*-20261001.csv` files. The original expressions and 2024--2026 year filters were checked on native result pages.

ACM recognized institutional Premium access. Title queries S03/S06/S09 returned **15/12/8 observations** in the **ACM Full-Text Collection**, using January 2024 through September 2026 e-publication dates. All observed result pages were recorded in `search-expansion-ACM-20261001.csv`. The Guide to Computing Literature was not searched, and these are rendered-page records rather than an ACM native export.

Google Scholar S01 was browsed through page 27. Only pages **19--27** of this expanded pass are retained in the two dated TSV files (90 observations). Earlier expanded pages were not saved before browser-session loss and are not claimed as preserved records. The original 30 September observations remain available separately. The displayed estimate of 756 results is approximate. Scholar pagination is incomplete, and S04/S07 have no additional retained pages in this checkpoint.

The additional exports contain **843 raw observations** and **817 provisionally consolidated candidate records** under the stated DOI/title rule. Raw observation and provisional identity counts differ from scientifically assessed studies. Complete title/abstract and primary-text screening has not been performed. See `search-completion-candidates.csv` and `search-completion-status.json` for current candidate states.

Of the **18 previously unresolved observations, 14 are now included, two are excluded for application scope, one is a secondary review, and one still requires primary text**. The original 50-record disposition is 38 included, one pending, three excluded, and eight other dispositions. The application collection now has **136 records (46 privacy, 58 consent/permission, 32 identity)**. The source-linked synthesis matrix has 67 records. The education chapter remains pending despite access working for other Springer sources. A focused full-text search found bibliographic/abstract records, without an accessible method-bearing copy.

Retrieval from Scopus and ACM is now documented. Additional-candidate scientific screening, Scholar pagination, and the remaining education chapter assessment are still incomplete. The current manuscript and dataset state these limits rather than treating retrieval alone as a completed method.

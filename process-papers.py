"""Modified 2026-10-01: audit legacy exports without deleting or merging records.

Use run.py for the current selected-study dataset. Historical exports are kept
unchanged; candidate duplicate groups are evidence for review, not exclusions.
"""
import json
from scripts.audit_legacy_exports import audit

if __name__ == '__main__':
    print(json.dumps(audit(), indent=2, ensure_ascii=False))

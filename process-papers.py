"""Report possible duplicate identities in the included publications."""
import json
from scripts.audit_publications import audit

if __name__ == '__main__':
    print(json.dumps(audit(), indent=2, ensure_ascii=False))

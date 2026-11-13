# Historical retrieval records

The `privacy/`, `consent/`, and `identity/` directories retain historical search exports. Their `google.csv`, `scopus.csv`, and `acm.csv` files are retrieval observations, not the current included-publication collection. Earlier merged outputs and figures are preserved for provenance.

`total_works_by_year.csv` contains historical 2015–2022 counts and includes federated learning. Use [studies-by-year.csv](../data/studies-by-year.csv) for the current 139 publications. Select either `extraction_year` or `bibliography_year`; summing both counts every publication twice.

## Earlier DOI processing defect

The earlier process concatenated retrieval rows, removed duplicates on DOI, and then removed exact-title duplicates. It treated missing DOI values as one repeated identifier. The recorded removal counts were:

| Family | Removed at DOI stage | Removed at later title stage | Remaining |
|---|---:|---:|---:|
| Privacy | 668 | 10 | 411 |
| Consent | 159 | 2 | 126 |
| Identity | 149 | 1 | 108 |

The earlier figure's duplicate labels correspond to DOI-stage removals, not unique records remaining. A missing DOI does not establish duplication. Correcting the current processing cannot reconstruct an undocumented historical selection. The 98 selected historical publications and all historical CSV files therefore retain their identities and contents.

The current collection adds 41 separately documented publications, producing 48 privacy, 59 consent, and 32 identity records. These included-publication totals are not reconstructed search totals.

## Read-only audit

`python3 process-papers.py` reads the nine source exports and prints candidate matches based on nonempty normalized DOIs and normalized titles. Each match includes its source file and record number. Title groups with conflicting nonempty DOIs are flagged.

Groups can overlap and are not automatically confirmed duplicates. The command removes no records and does not infer a corrected historical selection. The original processing is archived below from the commit identified by `legacy_base_commit` in [source-snapshot.json](../data/source-snapshot.json). That identifier records its origin in the earlier history; the current snapshot starts a new history.

## Archived original processing

This listing preserves the historical implementation for inspection. It contains the DOI defect described above and is not used by the current reproduction commands.

<details>
<summary>Original process-papers.py at 67acd264f6eeecbc9dda91d3027d1c875295f4ec</summary>

```python
import pandas as pd

def merge_csv_files(file1_path, file2_path, file3_path, output_path):
    # Load the first CSV file
    df1 = pd.read_csv(file1_path)

    # Load the second CSV file
    df2 = pd.read_csv(file2_path)
    
    
    df3 = pd.read_csv(file3_path)

    # Merge the two dataframes based on the DOI column
    df = pd.concat([df1, df2,df3])
    
    print("Shape:", df.shape)

    # Count the number of duplicates based on the "DOI" column
    num_duplicates_doi = df.duplicated(subset=['DOI']).sum()

    # Drop the duplicates based on the "DOI" column
    df = df.drop_duplicates(subset=['DOI'], keep='first')

    # Count the number of duplicates based on the "Title" column in the remaining dataset
    num_duplicates_title = df.duplicated(subset=['Title']).sum()

    # Drop the duplicates based on the "Title" column in the remaining dataset
    df = df.drop_duplicates(subset=['Title'], keep='first')

    # Write the result to a new CSV file
    df.to_csv(output_path, index=False)

    # Print the number of duplicates removed
    print(f"{output_path} / Total number of duplicates removed based on DOI: {num_duplicates_doi}")
    print(f"{output_path} / Total number of duplicates removed based on Title: {num_duplicates_title}")

# Define file paths
privacy_from_google = "privacy/google.csv"
privacy_from_scopus = "privacy/scopus.csv"
privacy_from_acm = "privacy/acm.csv"
privacy_output = "privacy/privacy_merged_dataset.csv"

consent_from_google = "consent/google.csv"
consent_from_scopus = "consent/scopus.csv"
consent_from_acm = "consent/acm.csv"
consent_output = "consent/consent_merged_dataset.csv"

identity_from_google = "identity/google.csv"
identity_from_scopus = "identity/scopus.csv"
identity_from_acm = "identity/acm.csv"
identity_output = "identity/fl_merged_dataset.csv"

# Merge privacy CSV files

print("\nData privacy:")
merge_csv_files(privacy_from_google, privacy_from_scopus, privacy_from_acm, privacy_output)
print(674+394+39)

# Merge consent CSV files

print("\nConsent data:")
merge_csv_files(consent_from_google, consent_from_scopus, consent_from_acm, consent_output)
print(164+88+45)

# Merge identity CSV files

print("\nIdentity data:")
merge_csv_files(identity_from_google, identity_from_scopus, identity_from_acm, identity_output)
print(209+104+6)



```

</details>

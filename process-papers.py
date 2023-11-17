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




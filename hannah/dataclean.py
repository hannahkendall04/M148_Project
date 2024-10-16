# Script to clean dataset and generate a new dataset with only the columns needed for the analysis (stored in clean_data.csv)
# Follows the same process as outline in data_clean.ipynb, but outputs a csv file

import pandas as pd

# Load the dataset
spotify_data_orig = pd.read_csv('../spotify_dataset.csv')

# Clean data
spotify_nona = spotify_data_orig.dropna()
no_dups = spotify_nona.drop_duplicates("track_id", keep="first")

# Check unique IDs
nrows = no_dups.shape[0]
nunique = no_dups['track_id'].nunique()

if nrows == nunique:
    print("No duplicates found!")
else:
    print("Duplicates found :-(")

clean_df = no_dups[no_dups['time_signature'] >= 3]

with pd.ExcelWriter('clean_data.xlsx') as writer:
    clean_df.to_excel(writer, sheet_name='Clean', index=False)

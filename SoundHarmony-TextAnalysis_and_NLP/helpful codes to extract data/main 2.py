import pandas as pd
import glob

# Path to the directory containing the CSV files
path = r'C:\Users\ADMIN\Desktop\TextAnalysis_project\data\*.csv'

# Use glob to match the pattern and get a list of file names
all_files = glob.glob(path)

# Initialize an empty list to hold the dataframes
dfs = []

# Iterate over the list of file names and read each CSV file into a dataframe
for filename in all_files:
    df = pd.read_csv(filename)
    dfs.append(df)

# Concatenate all dataframes in the list along axis 0 (row-wise) into one dataframe
combined_df = pd.concat(dfs, axis=0, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv(r'C:\Users\ADMIN\Desktop\TextAnalysis_project\RedditComments.csv', index=False)

print('Combined CSV file has been created successfully!')

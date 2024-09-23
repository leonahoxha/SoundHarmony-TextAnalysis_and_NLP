import pandas as pd

# Read the CSV file into a DataFrame
file_path = 'RedditComments.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Filter rows where "Headphone Name" is not equal to "bose quietcomfort ultra"
df = df[df['Headphone Name'] != 'bose quietcomfort ultra']

# Save the modified DataFrame back to the same CSV file
df.to_csv(file_path, index=False)

print(f"Filtered data saved to {file_path}")


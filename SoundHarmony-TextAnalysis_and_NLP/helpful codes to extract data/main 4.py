import pandas as pd

# Load the CSV file
reddit = pd.read_csv('RedditComments.csv')

# Remove rows where 'Comment' column is NaN
reddit.dropna(subset=['Comment'], inplace=True)

# Save the updated DataFrame back to the same CSV file
reddit.to_csv('RedditComments.csv', index=False)

print("CSV file updated successfully!")

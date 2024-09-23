import pandas as pd

# Read the CSV file into a DataFrame
file_name = 'data/steelseries_arctisnovapro.csv'
df = pd.read_csv(file_name)

# Add a new column "Headphone Name" with the value "jbl_endurancepeakii"
df.insert(0, 'Headphone Name', 'steelseries arctis nova pro')

# Save the modified DataFrame back to the original CSV file
df.to_csv(file_name, index=False)

print(f"The existing CSV file '{file_name}' has been updated with the 'Headphone Name' column.")
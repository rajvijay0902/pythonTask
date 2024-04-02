import re
import pandas as pd
import os
# Example usage
import os

# Get the absolute path of the current working directory
current_dir = os.getcwd()

# Extract the folder name from the absolute path
folder_name = os.path.basename(current_dir)

print("Current folder name:", folder_name)
# Function to extract timestamp from folder name
def extract_timestamp(folder_name):
    match = re.search(r'(\d{14})', folder_name)
    if match:
        return match.group(1)
    else:
        return None

# Function to process CSV file
def process_csv(folder_name):
    # Extract timestamp from folder name
    timestamp = extract_timestamp(folder_name)
    df = pd.read_csv("sample2.csv")

# Add a new column with the current timestamp
    df['Timestamp'] = timestamp
    print(df)
    df.to_csv('sample2.csv')
    return df



process_csv(folder_name)

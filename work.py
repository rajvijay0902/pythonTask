import re
import pandas as pd
import os


current_dir = os.getcwd()

folder_name = os.path.basename(current_dir)

print("Current folder name:", folder_name)
def extract_timestamp(folder_name):
    match = re.search(r'(\d{14})', folder_name)
    if match:
        return match.group(1)
    else:
        return None

def process_csv(folder_name):
    timestamp = extract_timestamp(folder_name)
    df = pd.read_csv("sample2.csv")
    df['Timestamp'] = timestamp
    print(df)
    df.to_csv('sample2.csv')
    return df



process_csv(folder_name)

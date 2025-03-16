import os
import pandas as pd

# Directory containing all CSV files
directory = "C:\\Users\\Asus\\Documents\\Music\\AppleMusic\\Scrape_data"  # Replace with the actual directory path
output_file = "merged_top_songs.csv"  # Name of the output file

# Initialize an empty DataFrame to store the merged data
merged_df = pd.DataFrame()

# Loop through each file in the directory
for filename in sorted(os.listdir(directory)):
    file_path = os.path.join(directory, filename)
    
    # Check if the file is a CSV
    if os.path.isfile(file_path) and filename.endswith('.csv'):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        # Add a new column for the filename (optional for tracking source files)
        df['Source File'] = filename
        # Append the data to the merged DataFrame
        merged_df = pd.concat([merged_df, df], ignore_index=True)

# Write the merged DataFrame to a single CSV file
merged_df.to_csv(output_file, index=False, encoding='utf-8')

print(f"All CSV files have been merged into {output_file}")

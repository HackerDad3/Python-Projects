import pandas as pd
import os

# Define the path to your Excel file and directory with files to be renamed
excel_file_path = 'C:\\Users\\Willi\\OneDrive\\Documents\\Python Projects\\My Code\\RenameKey.xlsx'
directory_path = 'C:\\Users\\Willi\\OneDrive\\Documents\\Python Projects\\My Code\\Delivery'

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    current_filename = row['Current Name']
    new_filename = row['New Name']
    current_filepath = os.path.join(directory_path, current_filename)
    new_filepath = os.path.join(directory_path, new_filename)

    # Check if the current file exists and rename it
    if os.path.exists(current_filepath):
        os.rename(current_filepath, new_filepath)
        print(f'Renamed: {current_filename} to {new_filename}')
    else:
        print(f'File not found: {current_filename}')

print('Bulk renaming complete.')

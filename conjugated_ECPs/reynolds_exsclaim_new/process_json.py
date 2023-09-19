import json
import os

def filter_json_by_folder(json_file_path, folder_path):
    # Read the JSON file into a dictionary
    with open(json_file_path, 'r') as f:
        json_dict = json.load(f)

    # List all files in the target folder
    folder_files = os.listdir(folder_path)

    # Filter the JSON dictionary to only include keys that have a corresponding file in the folder
    filtered_json_dict = {key: value for key, value in json_dict.items() if key in folder_files}

    # Write the filtered JSON dictionary back to file
    with open('filtered_' + os.path.basename(json_file_path), 'w') as f:
        json.dump(filtered_json_dict, f, indent=4)

if __name__ == '__main__':
    # Replace 'your_json_file.json' with the path to your JSON file
    # Replace 'your_folder_path' with the path to the folder you want to filter by
    filter_json_by_folder('exsclaim.json', 'figures')

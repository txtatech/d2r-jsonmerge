import os
import json

def append_json_files(directory, output_file):
    with open(output_file, 'a') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as infile:
                            json_data = json.load(infile)
                            json.dump(json_data, outfile)
                            outfile.write('\n')
                    except (ValueError, json.JSONDecodeError) as e:
                        print(f"Error reading file {file_path}: {str(e)}")

# Usage example
directory_path = r'E:\data'
output_file_path = r'E:\data\output.json'

append_json_files(directory_path, output_file_path)

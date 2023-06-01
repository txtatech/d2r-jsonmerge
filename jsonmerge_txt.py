import os
import shutil

def append_json_files(directory, output_file):
    with open(output_file, 'ab') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as infile:
                        shutil.copyfileobj(infile, outfile)
                    outfile.write(b'\n')  # Add a new line after each file

# Usage example
directory_path = r'E:\data'
output_file_path = r'E:\data\outputastext.txt'

append_json_files(directory_path, output_file_path)

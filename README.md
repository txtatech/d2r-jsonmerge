# d2r-jsonmerge
Merge Diablo II: Resurrected JSON files or copy their contents as plain text from a directory (including subdirectories) into a single output file.

**Use case:**

Merging the JSON files into a single file makes it easier to search their contents to help with modding.

These scripts allow you to merge all JSON files within a directory (including its subdirectories) into a single output file. They provide two options: JSON output and text output.

## JSON Output Script 'jsonmerge_json.py'

The JSON output script (`jsonmerge_json`) traverses the specified directory and appends the contents of each JSON file to a single output file, preserving the JSON structure. To use the script:

1. Replace the `directory_path` variable with the path to the directory containing the JSON files you want to merge.
2. Replace the `output_file_path` variable with the desired output file path.
3. Run the script using Python (`python jsonmerge_json.py`).

The JSON output script parses each JSON file, so ensure that all files are valid JSON documents. If any files have syntax errors, the script will raise an exception and indicate the problematic file.

## Text Output Script 'jsonmerge_txt.py'

The text output script (`jsonmerge_txt.py`) copies the raw contents of each JSON file as plain text without parsing it as JSON. This script is useful if you want to merge JSON files as plain text. To use the script:

1. Replace the `directory_path` variable with the path to the directory containing the JSON files you want to merge.
2. Replace the `output_file_path` variable with the desired output file path.
3. Run the script using Python (`python jsonmerge_txt.py`).

The text output script copies the byte contents of each JSON file, preserving the encoding and formatting of the original files.

**Note:** Both scripts have the potential to produce very large output files, especially if the directory contains numerous or large JSON files. Take this into consideration when running the scripts and ensure that you have enough disk space available to accommodate the merged output file.

It is recommended to test the scripts on a smaller dataset or use appropriate filtering to merge specific files before attempting to merge a large number of files.

## Dependency Note

The provided scripts (`jsonmerge_json.py` and `jsonmerge_txt.py`) have no external dependencies or additional packages required. They utilize built-in Python modules, such as `os`, `shutil`, and `json` (only for `json_merge.py`), which are part of the Python Standard Library. 

To run the scripts, ensure that you have a valid Python installation, which includes these modules by default.


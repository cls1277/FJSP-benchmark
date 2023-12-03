import os
import json

# Specify folder path
folder_path = os.path.dirname(__file__)

# Initialize an empty dictionary to store file information
file_info_dict = {}

# Iterate through files in a folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.fjs'):
        # Full path to build file
        file_path = os.path.join(folder_path, file_name)

        # Read the file contents and extract the first and second space-separated numbers
        with open(file_path, 'r') as file:
            content = file.read()
            numbers = content.split()
            
            # Use the first and second numbers for jobs and machines
            jobs, machines = map(int, (numbers[0], numbers[1]))

        # Store file information in a dictionary
        file_info_dict[file_name] = {
            'name': file_name[:-4],
            'jobs': jobs,
            'machines': machines,
            'path': folder_path[51:]+"/"+file_name
            # Additional information can be added, such as file content, etc.
        }

# Sort dictionary lexicographically by keys
sorted_file_info = dict(sorted(file_info_dict.items()))

# Extract the values of the sorted dictionary as the contents of the JSON file
values_only = list(sorted_file_info.values())

# Write values to JSON file
output_json_path = 'instances.json'
with open(output_json_path, 'w') as json_file:
    json.dump(values_only, json_file, indent=2)

print(f"File information has been written to the dictionary in lexicographic order by dictionary key {output_json_path}")

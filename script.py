import os
import json

# Main folder path
main_folder_path = os.path.dirname(__file__)

# Initialize an empty dictionary to store file information
all_file_info_dict = []

# Traverse all sub folders under the main folder
for subfolder_name in os.listdir(main_folder_path):
    subfolder_path = os.path.join(main_folder_path, subfolder_name)

    # Check if it is a folder
    if os.path.isdir(subfolder_path):
        # Initialize an empty dictionary to store file information in the current subfolder
        file_info_dict = {}

        # Traverse the. fjs files in the current subfolder
        for file_name in os.listdir(subfolder_path):
            if file_name.endswith('.fjs'):
                file_path = os.path.join(subfolder_path, file_name)

                # Read the file content and extract the first and second numbers separated by spaces
                with open(file_path, 'r') as file:
                    content = file.read()
                    numbers = content.split()

                    # Use the first and second numbers as jobs and machines
                    jobs, machines = map(int, (numbers[0], numbers[1]))

                # Store file information in the dictionary of the current subfolder
                file_info_dict[file_name] = {
                    'name': file_name[:-4],
                    'jobs': jobs,
                    'machines': machines,
                    'path': subfolder_name+"/"+file_name
                    # Additional information can be added, such as file content, etc
                }

        # Sort the dictionaries of the current sub folder according to the dictionary order of the key
        sorted_file_info = dict(sorted(file_info_dict.items()))

        # Add the sorted dictionary values to the overall list
        all_file_info_dict.extend(list(sorted_file_info.values()))

# Write the overall list into a JSON file
output_json_path = 'instances.json'
with open(output_json_path, 'w') as json_file:
    json.dump(all_file_info_dict, json_file, indent=2)

print(f"All file information has been written in the dictionary order {output_json_path}")

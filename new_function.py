import os
import random

def combine_all_text_files(folder_path, number_of_files):
    # Get all file names in the folder

    all_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    # Randomly select the specified number of text files
    selected_files = random.sample(all_files, min(len(all_files), number_of_files))
    
    # Initialize a variable to store the concatenated content
    combined_content = ""
    
    # Loop through each selected file, read its content, and append to the combined_content variable
    for file_name in selected_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Append the file content to the combined_content variable, separated by a space
            combined_content += content + " "
    
    return combined_content

# Example usage
folder_path = os.path.join(os.path.dirname(__file__), 'Sports')
number_of_files = 6000
combined_content = combine_all_text_files(folder_path, number_of_files)


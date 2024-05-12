# Data cleaning tool used to transform the .txt files found in './uncleanedData' to the .txt files found in './cleanedData'

import os
import re

def clean_text(text):
    # Remove special characters, extra whitespaces, and any hyperlinks
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = re.sub(r'https://\S+', '', cleaned_text)
    return cleaned_text.strip()

def clean_files(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all files in the input directory
    files = os.listdir(input_dir)

    # Iterate over each file
    for file_name in files:
        # Construct the full file paths
        input_file_path = os.path.join(input_dir, file_name)
        output_file_path = os.path.join(output_dir, file_name)
        
        # Check if the path is a file (not a directory) and if it's a text file
        if os.path.isfile(input_file_path) and file_name.endswith('.txt'):
            # Open the input file in read mode
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                # Read the content
                content = input_file.read()
            
            # Clean the content
            cleaned_content = clean_text(content)
            
            # Write the cleaned content to the output file
            with open(output_file_path, 'w') as output_file:
                output_file.write(cleaned_content)

# Example usage
input_directory = './cleanedData'
output_directory = './cleanedData'
clean_files(input_directory, output_directory)
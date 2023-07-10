import os
from fuzzywuzzy import fuzz

text_file_path = 'lists.txt'
directory_path = 'E:\\Sabir Data\\VueSchool.io Premium\\The Vue.js 3 Masterclass'

# Read the content of the text file
with open(text_file_path, 'r') as file:
    lines = file.readlines()

# Process each line in the text file
for line in lines:
    line = line.strip()
    # Skip empty lines
    if not line:
        continue

    # Split the line by the first occurrence of a dot followed by a space
    split_line = line.split('. ', 1)
    if len(split_line) != 2:
        # Line doesn't match the expected format, skip it
        continue

    number, title = split_line
    try:
        number = int(number)
    except ValueError:
        # Line doesn't start with a valid number, skip it
        continue

    # Remove whitespace and convert to lowercase for matching
    title = title.strip().lower().replace(' ', '')

    # Find the corresponding file in the directory
    best_match = None
    best_match_score = -1
    for filename in os.listdir(directory_path):
        # Remove whitespace and convert to lowercase for matching
        filename_cleaned = filename.lower().replace(' ', '')

        # Calculate the matching score between the title and the filename
        match_score = fuzz.ratio(title, filename_cleaned)
        if match_score > best_match_score:
            best_match = filename
            best_match_score = match_score

    if best_match is not None:
        # Rename the file with the number
        new_filename = f'{number}. {best_match}'
        old_filepath = os.path.join(directory_path, best_match)
        new_filepath = os.path.join(directory_path, new_filename)
        os.rename(old_filepath, new_filepath)

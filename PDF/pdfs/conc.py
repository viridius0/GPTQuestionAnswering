import os
import re
import sys

# Get the directory path from command line argument
if len(sys.argv) < 2:
    print("Please provide the directory path as an argument.")
    sys.exit()
dir_path = sys.argv[1]

# Find all text files in the directory and sort them by the codified numbering system
text_files = [f for f in os.listdir(dir_path) if f.endswith('.txt')]
text_files.sort(key=lambda x: [int(i) if i.isdigit() else i for i in re.findall(r'\d+|\D+', x)])

# Open the output file for writing
output_file = open("RCW-Final.txt", "w")

# Loop through all sorted text files and concatenate their contents to the output file
for filename in text_files:
    # Open the text file and read its contents
    with open(os.path.join(dir_path, filename), "r") as text_file:
        text = text_file.read()

    # Append the resulting text to the output file
    output_file.write(text)

# Close the output file
output_file.close()

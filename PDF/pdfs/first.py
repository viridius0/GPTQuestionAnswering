import os
import re

# Get the directory path from command line argument
dir_path = input("Please provide the directory path: ")

# Find all TXT files in the directory and sort them by the codified numbering system
txt_files = [f for f in os.listdir(dir_path) if f.endswith('.txt')]
txt_files.sort(key=lambda x: [int(i) for i in re.findall(r'\d+', x)])

# Open the output file for writing
output_file = open("RCW-FirstLines.txt", "w")

# Loop through all sorted TXT files and write their first lines to the output file
for filename in txt_files:
    # Read the first line of the file
    with open(os.path.join(dir_path, filename), "r") as file:
        first_line = file.readline()

    # Write the first line to the output file
    output_file.write(first_line)

# Close the output file
output_file.close()

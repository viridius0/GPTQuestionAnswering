import os
import re
import sys
from tika import parser

# Get the directory path from command line argument
if len(sys.argv) < 2:
    print("Please provide the directory path as an argument.")
    sys.exit()
dir_path = sys.argv[1]

# Create the "tmp" directory if it doesn't exist
if not os.path.exists("tmp"):
    os.makedirs("tmp")

# Find all PDF files in the directory and sort them by the codified numbering system
pdf_files = [f for f in os.listdir(dir_path) if f.endswith('.pdf')]
pdf_files.sort(key=lambda x: [int(i) for i in re.findall(r'\d+', x)])

# Loop through all sorted PDF files and write their contents to individual text files in the "tmp" directory
for filename in pdf_files:
    # Parse the PDF and extract the text
    parsed = parser.from_file(os.path.join(dir_path, filename))
    text = parsed['content']

    # Remove the specified pattern
    text = re.sub(r"\n\[\s*\d+\s*\]\n+", "", text)
    text = text.lstrip()
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    # Write the resulting text to a new file with the same name as the PDF but with a ".txt" extension
    with open(os.path.join("tmp", os.path.splitext(filename)[0] + ".txt"), "w") as f:
        f.write(text)


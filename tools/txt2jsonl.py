import jsonlines
import sys

# Check if input file was provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)

# Get input file name from command-line argument
input_file = sys.argv[1]

# Open input file for reading
with open(input_file, 'r') as f_in:
    # Read the input file line by line
    for line in f_in:
        # Strip any leading or trailing whitespace from the line
        line = line.strip()

        # Get the id and title from the line
        id_title = line.split(' ', 2)[1]  # Assumes id and title are the second string between spaces

        # Create a dictionary with the "id", "title", "text", and "section" keys
        data = {
            "id": id_title,
            "title": id_title,
            "text": line,
            "section": ""
        }

        # Write the data as a single JSONL entry to stdout
        writer = jsonlines.Writer(sys.stdout)
        writer.write(data)


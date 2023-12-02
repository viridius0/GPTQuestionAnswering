import argparse
import json

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Path to the input JSON lines file")
parser.add_argument("output_file", help="Path to the output JSON lines file")
args = parser.parse_args()

# Open the input and output files
with open(args.input_file, "r") as f_in, open(args.output_file, "w") as f_out:
    # Loop over each line in the input file
    for line in f_in:
        # Parse the line as a JSON object
        obj = json.loads(line)

        # Convert the "Embeddings" tag from a list of lists to a single list
        embeddings = [e for window in obj["Embeddings"] for e in window]

        # Add a new tag to the object with the new embeddings
        obj["Embeddings"] = embeddings

        # Write the updated object to the output file as a JSON string
        f_out.write(json.dumps(obj) + "\n")

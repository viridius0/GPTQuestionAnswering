import json

input_file = "output.jsonl"
output_file = "output.para"

with open(input_file, "r") as input, open(output_file, "w") as output:
    for line in input:
        data = json.loads(line)
        output.write(data["Title"] + "\t" + data["Text"] + "\n")

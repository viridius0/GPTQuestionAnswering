import json

input_file = 'output-embed.jsonl'

with open(input_file, 'r') as f:
    for i, line in enumerate(f):
        data = json.loads(line)
        if 'Embeddings' not in data or not data['Embeddings']:
            print(f"Line {i+1} has an empty or missing 'Embeddings' tag")

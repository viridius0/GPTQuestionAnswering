import json

input_file = 'output-minus.jsonl'
output_file = 'output.jsonl'

with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
        data = json.loads(line)
        if 'Embeddings' in data:
            del data['Embeddings']
        if 'Tokens' in data:
            del data['Tokens']
        f_out.write(json.dumps(data) + '\n')

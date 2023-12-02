import json

input_file = 'output.jsonl'
output_file = 'output-minus.jsonl'

with open(output_file, 'w') as out_file:
    with open(input_file, 'r') as in_file:
        for line in in_file:
            data = json.loads(line.strip())
            if 'FAISSID' in data:
                data['FAISSID'] -= 1
            out_file.write(json.dumps(data) + '\n')

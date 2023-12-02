import json

input_file = 'output-embed.jsonl'
output_file = 'output-embed-fixed.jsonl'

with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
        data = json.loads(line)
        id_string = data['ID']
        id_string_mod = id_string.replace('-', '.')
        data['ID'] = id_string_mod
        json.dump(data, f_out)
        f_out.write('\n')

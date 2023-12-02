import json
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    faiss_id = 1
    for line in f_in:
        data = json.loads(line)
        data['FAISSID'] = faiss_id
        f_out.write(json.dumps(data) + '\n')
        faiss_id += 1

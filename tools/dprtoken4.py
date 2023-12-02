from transformers import DPRContextEncoderTokenizer
import json

# Initialize the tokenizer
tokenizer = DPRContextEncoderTokenizer.from_pretrained("facebook/dpr-ctx_encoder-multiset-base")

# Set window size and stride
window_size = 256
stride = 236

# Open the input jsonl file and output file
with open("RCW-Final.jsonl", "r") as f_in, open("output.jsonl", "w") as f_out:
    # Loop over each line in the input file
    for line in f_in:
        # Parse the line as a JSON object
        obj = json.loads(line)

        # Extract the text field and title field
        text = obj["text"]
        title = obj["title"]

        # Tokenize the text using the tokenizer
        tokens = tokenizer.tokenize(text)

        # Split the tokens into windows
        windows = [tokens[i:i+window_size] for i in range(0, len(tokens)-window_size+1, stride)]

        # Add a new tag to the object with the tokenized windows, title, and untokenized text
        for i, window in enumerate(windows):
            new_obj = {}
            new_obj["ID"] = f"{title}-{i+1}"
            new_obj["Title"] = title
            new_obj["Tokens"] = window
            new_obj["Text"] = tokenizer.convert_tokens_to_string(window)

            # Write the updated object to the output file as a JSON string
            f_out.write(json.dumps(new_obj) + "\n")


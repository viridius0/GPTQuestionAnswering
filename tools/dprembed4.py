from transformers import DPRContextEncoder, DPRContextEncoderTokenizer
import json
import torch


tokenizer = DPRContextEncoderTokenizer.from_pretrained("facebook/dpr-ctx_encoder-multiset-base")
model = DPRContextEncoder.from_pretrained("facebook/dpr-ctx_encoder-multiset-base")
# Set the window size
window_size = 256

# Open the input JSON lines file and output file
with open("output.jsonl", "r") as f_in, open("output-embed.jsonl", "w") as f_out:
    # Loop over each line in the input file
    for line in f_in:
        # Parse the line as a JSON object
        obj = json.loads(line)

        # Extract the tokens from the "Tokens" tag
        tokens = obj["Tokens"]

        # Create sub-lists of tokens, each containing 256 tokens or less
        token_windows = [tokens[i:i+window_size] for i in range(0, len(tokens), window_size)]

        # Embed each token window individually
        embeddings = []
        for token_window in token_windows:
            input_ids = tokenizer.convert_tokens_to_ids(token_window)
            input_ids = torch.tensor(input_ids)
            window_embedding = model(input_ids.unsqueeze(0)).pooler_output.tolist()[0]
            embeddings.append(window_embedding)

        # Add a new tag to the object with the embeddings
        obj["Embeddings"] = embeddings

        # Write each embedding to a new line in the output file as a JSON string
        f_out.write(json.dumps(obj) + "\n")


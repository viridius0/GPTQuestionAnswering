import json
import numpy as np
import faiss
import torch
from transformers import DPRQuestionEncoder, DPRConfig
from transformers import AutoTokenizer

# Load the Faiss index
index = faiss.read_index("index.faiss")

# Load the DPR question encoder model and tokenizer
model_name = "facebook/dpr-question_encoder-multiset-base"
config = DPRConfig.from_pretrained(model_name)
question_encoder = DPRQuestionEncoder.from_pretrained(model_name, config=config)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set up the GPU if available
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

# Define a function to encode a question using the DPR question encoder and GPU
def encode_question(question):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    question_encoder.to(device)
    inputs = tokenizer(question, return_tensors="pt").to(device)
    embeddings = question_encoder(inputs["input_ids"], inputs["attention_mask"])[0]
    embeddings = embeddings.detach().cpu().numpy()
    return embeddings

# Define a function to search the index given an encoded question
def search_index(query_embedding, k):
    _vector = np.array([query_embedding])
    faiss.normalize_L2(_vector)
    D, I = index.search(_vector, k)
    I = I.tolist()[0]  # convert the result to a list of IDs
    return D[0], I

# Start the query loop
while True:
    # Get a question from the user
    print(index.d)
    question = input("Query: ")

    # Encode the question
    query_embedding = encode_question(question)

    # Search the index
    k = 10  # number of results to return
    distances, I = search_index(query_embedding.flatten(), k)

    # Print the top 10 internal IDs of the matched embeddings
    retrieved_examples = ds_with_embeddings.get_nearest_examples('embeddings', query_embedding, k=10)
    print(json.dumps(retrieved_examples["line"]))


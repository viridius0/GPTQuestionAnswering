import json
import numpy as np
import faiss

# Load the embeddings from file
embeddings = []
faiss_ids = []
with open("output-embed.jsonl", "r") as f:
    for i, line in enumerate(f):
        data = json.loads(line)
        embedding = data["Embeddings"]
        embeddings.append(embedding)
        faiss_ids.append(i)

# Convert the embeddings and IDs to numpy arrays
embeddings = np.array(embeddings, dtype=np.float32)
faiss_ids = np.array(faiss_ids)

# Build the Faiss index
d = embeddings.shape[1]  # the dimension of the embeddings
nlist = 1000  # number of cells in the quantizer
quantizer = faiss.IndexFlatL2(d)  # the quantizer
index = faiss.IndexIVFFlat(quantizer, d, nlist)
print(index.is_trained)  # should print False

# Train the index
index.train(embeddings)
print(index.ntotal)  # should print 0
print(index.is_trained)  # should print True

# Add the embeddings to the index
index.add_with_ids(embeddings, faiss_ids)
print(index.ntotal)  # should print the number of embeddings in the index

# Save the index to a file
faiss.write_index(index, "index.faiss")


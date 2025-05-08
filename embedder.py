import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Assuming you have text chunks available in `texts`
# If the embeddings are not already generated, generate them:
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(texts, convert_to_numpy=True)

# Create a FAISS index
faiss_index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 distance metric
faiss_index.add(embeddings)  # Add embeddings to the FAISS index

# Save the index to a file
faiss.write_index(faiss_index, "faiss.idx")
print("FAISS index saved successfully!")

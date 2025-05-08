import openai
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

openai.api_key = "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"

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("faiss.idx")
texts = np.load("texts.npy", allow_pickle=True)
metas = np.load("metas.npy", allow_pickle=True)

def search_faiss(query, k=3):
    q_emb = model.encode([query])
    D, I = index.search(q_emb, k)
    return [texts[i] for i in I[0]], [metas[i] for i in I[0]]

def query_llm(question):
    contexts, pages = search_faiss(question)
    print("Contexts:", contexts)
    if contexts:
        prompt = f"Use the context to answer:\n\n{contexts[0]}\n\nQ: {question}\nA:"
    else:
        prompt = f"Q: {question}\nA: Sorry, no relevant context found."
    
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content'], pages[0]['page']


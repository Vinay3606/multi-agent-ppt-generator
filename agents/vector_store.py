from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# Model load
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_chunks(text, chunk_size=500, overlap=50):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start = end - overlap

    return chunks


def create_vector_store(text):

    chunks = create_chunks(text)

    embeddings = model.encode(chunks)

    embeddings = np.array(embeddings).astype("float32")

    # Cosine similarity ke liye normalize
    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    return index, chunks


def search_vector_store(query, index, chunks, top_k=3):

    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(query_embedding, top_k)

    results = []

    for score, idx in zip(scores[0], indices[0]):

        results.append({
            "content": chunks[idx],
            "score": float(score)
        })

    return results
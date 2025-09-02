from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load a pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Break big text into smaller chunks
def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

# Find most relevant parts of text for a query
def get_relevant_chunks(query, text, top_k=3):
    chunks = chunk_text(text)

    # Convert query and chunks into vectors
    query_embedding = model.encode([query])
    chunk_embeddings = model.encode(chunks)

    # Compare similarity
    scores = cosine_similarity(query_embedding, chunk_embeddings)[0]

    # Pick top-k chunks
    sorted_indexes = scores.argsort()[::-1]  # high → low
    best_chunks = [chunks[i] for i in sorted_indexes[:top_k]]

    return best_chunks

"""
Lesson 59: Vector Embeddings — Solutions
"""

import numpy as np
import hashlib
import json


def fake_embedding(text: str, dims: int = 64) -> list:
    seed = int(hashlib.md5(text.lower().strip().encode()).hexdigest(), 16) % (2**32)
    np.random.seed(seed)
    vec = np.random.randn(dims)
    vec = vec / np.linalg.norm(vec)
    return vec.tolist()

get_embedding = fake_embedding

KNOWLEDGE_BASE = [
    "Python is a high-level, interpreted programming language.",
    "NumPy provides N-dimensional array objects for numerical computing.",
    "The OpenAI API allows you to call GPT models programmatically.",
    "FastAPI is used to build REST APIs quickly with automatic documentation.",
    "Vector embeddings represent semantic meaning as numerical vectors.",
    "Pandas is a data analysis library for working with tabular data.",
    "The Eiffel Tower is a wrought-iron lattice tower in Paris.",
    "LangChain is a framework for building LLM-powered applications.",
    "Git is a distributed version control system.",
    "Machine learning models are trained on data to make predictions.",
]


# SOLUTION 1: Cosine Similarity
def cosine_similarity(a: list, b: list) -> float:
    a_arr = np.array(a)
    b_arr = np.array(b)
    return float(np.dot(a_arr, b_arr) / (np.linalg.norm(a_arr) * np.linalg.norm(b_arr)))


print("=" * 50)
print("Cosine Similarity")
print("=" * 50)
vec1 = get_embedding("machine learning")
vec2 = get_embedding("machine learning")
print(f"Same text: {cosine_similarity(vec1, vec2):.4f}")
vec3 = get_embedding("Python programming")
vec4 = get_embedding("banana bread recipe")
print(f"Different text: {cosine_similarity(vec3, vec4):.4f}")


# SOLUTION 2: Semantic Search
def semantic_search(query: str, documents: list, top_k: int = 3) -> list:
    query_emb = get_embedding(query)
    scored = []
    for doc in documents:
        doc_emb = get_embedding(doc)
        score = cosine_similarity(query_emb, doc_emb)
        scored.append((score, doc))
    scored.sort(reverse=True)
    return scored[:top_k]


print("\n" + "=" * 50)
print("Semantic Search")
print("=" * 50)
for query in ["How do I build a web API?", "What library for math and arrays?"]:
    print(f"\nQuery: '{query}'")
    for score, doc in semantic_search(query, KNOWLEDGE_BASE, top_k=2):
        print(f"  [{score:.3f}] {doc}")


# SOLUTION 3: Vector Database
class SimpleVectorDB:
    def __init__(self):
        self._documents = []
    
    def add(self, text: str, metadata: dict = None):
        embedding = get_embedding(text)
        self._documents.append({
            "text": text,
            "embedding": embedding,
            "metadata": metadata or {}
        })
    
    def search(self, query: str, top_k: int = 5) -> list:
        query_emb = np.array(get_embedding(query))
        scored = []
        for item in self._documents:
            vec = np.array(item["embedding"])
            score = float(np.dot(query_emb, vec) / (np.linalg.norm(query_emb) * np.linalg.norm(vec)))
            scored.append({**item, "score": score})
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]
    
    def __len__(self):
        return len(self._documents)
    
    def clear(self):
        self._documents = []


print("\n" + "=" * 50)
print("Vector Database")
print("=" * 50)
db = SimpleVectorDB()
for doc in KNOWLEDGE_BASE:
    db.add(doc, metadata={"source": "knowledge_base"})
print(f"Size: {len(db)} documents")
results = db.search("How do I build a web API?", top_k=3)
print("\nTop 3 results:")
for r in results:
    print(f"  [{r['score']:.3f}] {r['text']}")


# SOLUTION 4: Document Chunker
def chunk_text(text: str, chunk_size: int = 100, overlap: int = 20) -> list:
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start += chunk_size - overlap
    return chunks


print("\n" + "=" * 50)
print("Document Chunking")
print("=" * 50)
long_doc = "Python is great. " * 200
chunks = chunk_text(long_doc, chunk_size=50, overlap=10)
print(f"~{len(long_doc.split())} words → {len(chunks)} chunks")
print(f"Chunk 1: {chunks[0][:80]}...")

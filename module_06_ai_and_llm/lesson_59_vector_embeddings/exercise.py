"""
Lesson 59: Vector Embeddings — Exercise File

Build a simple semantic search engine using fake embeddings.
No API key needed — uses deterministic mock embeddings.
When ready: replace fake_embedding() with real OpenAI embeddings.
"""

import numpy as np
import hashlib
import json
from pathlib import Path


# ============================================================
# MOCK EMBEDDING FUNCTION
# Replace with real OpenAI embeddings when you have an API key:
#
# from openai import OpenAI
# client = OpenAI()
# def get_embedding(text):
#     return client.embeddings.create(model="text-embedding-3-small", input=text).data[0].embedding
# ============================================================

def fake_embedding(text: str, dims: int = 64) -> list:
    """
    Deterministic fake embedding for testing.
    Preserves structure (unit vector, correct dims) but not real semantics.
    """
    seed = int(hashlib.md5(text.lower().strip().encode()).hexdigest(), 16) % (2**32)
    np.random.seed(seed)
    vec = np.random.randn(dims)
    vec = vec / np.linalg.norm(vec)
    return vec.tolist()

get_embedding = fake_embedding  # Swap this for real embeddings


# ===========================================================
# EXERCISE 1: Cosine Similarity
# ===========================================================
# TODO: Implement cosine_similarity(a, b) that takes two lists of floats
# and returns a float between -1 and 1.
# Use numpy for the computation.

def cosine_similarity(a: list, b: list) -> float:
    """Calculate cosine similarity between two embedding vectors."""
    # YOUR CODE HERE
    pass


print("=" * 50)
print("Exercise 1: Cosine Similarity")
print("=" * 50)

# Test with identical vectors (should be ~1.0)
vec1 = get_embedding("machine learning")
vec2 = get_embedding("machine learning")
print(f"Same text similarity: {cosine_similarity(vec1, vec2):.4f} (expected: ~1.0)")

# Test with different vectors
vec3 = get_embedding("Python programming")
vec4 = get_embedding("banana bread recipe")
if cosine_similarity(vec3, vec4) is not None:
    print(f"Different text similarity: {cosine_similarity(vec3, vec4):.4f}")


# ===========================================================
# EXERCISE 2: Semantic Search
# ===========================================================
# TODO: Implement semantic_search(query, documents, top_k) that:
# 1. Embeds the query
# 2. Embeds each document
# 3. Computes cosine similarity between query and each doc
# 4. Returns top_k (document, similarity_score) tuples, sorted best first

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

def semantic_search(query: str, documents: list, top_k: int = 3) -> list:
    """
    Find top_k most relevant documents for the query.
    Returns list of (score, document) tuples.
    """
    # YOUR CODE HERE
    pass


print("\n" + "=" * 50)
print("Exercise 2: Semantic Search")
print("=" * 50)

queries = [
    "How do I build a web API?",
    "What library should I use for math and arrays?",
    "How do I call a language model from Python?",
]

for query in queries:
    print(f"\nQuery: '{query}'")
    results = semantic_search(query, KNOWLEDGE_BASE, top_k=2)
    if results:
        for score, doc in results:
            print(f"  [{score:.3f}] {doc}")


# ===========================================================
# EXERCISE 3: Simple Vector Database
# ===========================================================
# TODO: Implement a SimpleVectorDB class that:
# - Stores documents + embeddings in a list
# - add(text, metadata=None): embed and store a document
# - search(query, top_k=5): return top_k most similar docs
# - __len__: return number of documents
# - clear(): remove all documents

class SimpleVectorDB:
    """In-memory vector database for semantic search."""
    
    def __init__(self):
        self._documents = []  # list of {"text": ..., "embedding": ..., "metadata": ...}
    
    def add(self, text: str, metadata: dict = None):
        """Add a document to the database."""
        # YOUR CODE HERE
        pass
    
    def search(self, query: str, top_k: int = 5) -> list:
        """Find top_k most similar documents to query. Returns list of dicts."""
        # YOUR CODE HERE
        pass
    
    def __len__(self):
        # YOUR CODE HERE
        pass
    
    def clear(self):
        """Remove all documents."""
        # YOUR CODE HERE
        pass


print("\n" + "=" * 50)
print("Exercise 3: Vector Database")
print("=" * 50)

db = SimpleVectorDB()

# Add documents
for doc in KNOWLEDGE_BASE:
    db.add(doc, metadata={"source": "knowledge_base"})

print(f"Database size: {len(db)} documents")

# Search
results = db.search("How do I build a web API?", top_k=3)
if results:
    print("\nSearch results for 'How do I build a web API?':")
    for r in results:
        print(f"  [{r.get('score', 0):.3f}] {r.get('text', '')}")


# ===========================================================
# EXERCISE 4: Document Chunker
# ===========================================================
# TODO: Implement chunk_text(text, chunk_size=100, overlap=20) that:
# - Splits text into chunks of approximately chunk_size words
# - Overlaps adjacent chunks by `overlap` words
# - Returns a list of strings

def chunk_text(text: str, chunk_size: int = 100, overlap: int = 20) -> list:
    """
    Split text into overlapping chunks.
    chunk_size: approximate words per chunk
    overlap: words to repeat between adjacent chunks
    """
    # YOUR CODE HERE
    pass


print("\n" + "=" * 50)
print("Exercise 4: Document Chunking")
print("=" * 50)

long_doc = """
Python is a high-level, general-purpose programming language. Its design philosophy 
emphasizes code readability, and its syntax allows programmers to express concepts in 
fewer lines of code than would be possible in languages such as C++ or Java. Python 
supports multiple programming paradigms, including structured, object-oriented, and 
functional programming. It was created by Guido van Rossum and first released in 1991.
Python consistently ranks as one of the most popular programming languages, and its 
applications range from web development and data science to machine learning and automation.
The language has a comprehensive standard library and a vibrant ecosystem of third-party 
packages available through the Python Package Index (PyPI).
""" * 3  # Repeat 3x to make it longer

chunks = chunk_text(long_doc, chunk_size=50, overlap=10)
if chunks:
    print(f"Document of ~{len(long_doc.split())} words split into {len(chunks)} chunks")
    print(f"Chunk 1 ({len(chunks[0].split())} words): {chunks[0][:100]}...")
    if len(chunks) > 1:
        print(f"Chunk 2 ({len(chunks[1].split())} words): {chunks[1][:100]}...")

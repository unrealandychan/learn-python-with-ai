# Lesson 59: Vector Embeddings — How AI Understands Meaning

Vector embeddings are numerical representations of text (or images, audio, etc.) that capture semantic meaning. They are the foundation of:
- Semantic search
- Recommendation systems
- RAG (Retrieval-Augmented Generation)
- Document clustering
- Anomaly detection

## What is an Embedding?

An embedding is a list of floating-point numbers (a vector) that represents the "meaning" of a piece of text:

```python
# "Python programming" might be represented as:
embedding = [0.21, -0.84, 0.12, 0.73, ..., -0.45]  # 1536 numbers for text-embedding-3-small
```

**Key property**: Texts with similar meaning have vectors that point in similar directions (high cosine similarity).

## Getting Embeddings with OpenAI

```python
from openai import OpenAI

client = OpenAI()

def get_embedding(text: str, model: str = "text-embedding-3-small") -> list[float]:
    """Get a vector embedding for a piece of text."""
    response = client.embeddings.create(
        model=model,
        input=text
    )
    return response.data[0].embedding

# Returns a list of 1536 floats
embedding = get_embedding("The quick brown fox")
print(f"Dimensions: {len(embedding)}")   # 1536
print(f"First 5 values: {embedding[:5]}")
```

## Semantic Search

Find the most relevant documents for a query:

```python
import numpy as np
from openai import OpenAI

client = OpenAI()

def cosine_similarity(a: list[float], b: list[float]) -> float:
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def semantic_search(query: str, documents: list[str], top_k: int = 3) -> list[tuple]:
    """Find the most semantically similar documents to a query."""
    # Embed the query
    query_embedding = get_embedding(query)
    
    # Embed all documents (in practice, you'd cache these)
    results = []
    for doc in documents:
        doc_embedding = get_embedding(doc)
        similarity = cosine_similarity(query_embedding, doc_embedding)
        results.append((similarity, doc))
    
    # Sort by similarity (highest first)
    results.sort(reverse=True)
    return results[:top_k]

# Example:
knowledge_base = [
    "Python was created by Guido van Rossum in 1991.",
    "NumPy provides fast array operations for scientific computing.",
    "FastAPI is a modern web framework for building APIs.",
    "The Eiffel Tower is located in Paris, France.",
    "Machine learning models learn patterns from data.",
]

results = semantic_search("How do I build a REST API in Python?", knowledge_base)
for score, doc in results:
    print(f"{score:.3f}: {doc}")
```

## Building a Simple Vector Database

```python
import json
import numpy as np
from pathlib import Path

class SimpleVectorDB:
    """A minimal vector database that stores embeddings on disk."""
    
    def __init__(self, path: str = "vector_db.json"):
        self.path = Path(path)
        self.data = self._load()
    
    def _load(self) -> list[dict]:
        if self.path.exists():
            with open(self.path) as f:
                return json.load(f)
        return []
    
    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f)
    
    def add(self, text: str, embedding: list[float], metadata: dict = None):
        """Add a document with its embedding."""
        self.data.append({
            "text": text,
            "embedding": embedding,
            "metadata": metadata or {}
        })
        self._save()
    
    def search(self, query_embedding: list[float], top_k: int = 5) -> list[dict]:
        """Find top-k most similar documents."""
        q = np.array(query_embedding)
        
        scored = []
        for item in self.data:
            vec = np.array(item["embedding"])
            similarity = np.dot(q, vec) / (np.linalg.norm(q) * np.linalg.norm(vec))
            scored.append({"score": float(similarity), **item})
        
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]
    
    def __len__(self):
        return len(self.data)
```

## Chunking Documents

Long documents need to be split into smaller chunks before embedding:

```python
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    Split text into overlapping chunks.
    Overlap ensures context isn't lost at chunk boundaries.
    """
    words = text.split()
    chunks = []
    start = 0
    
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        
        if end == len(words):
            break
        start += chunk_size - overlap  # overlap creates context continuity
    
    return chunks

# Example:
long_doc = "word " * 1000  # 1000-word document
chunks = chunk_text(long_doc, chunk_size=100, overlap=20)
print(f"Document split into {len(chunks)} chunks")
```

## Embedding Dimensions

| Model | Dimensions | Use Case |
|-------|-----------|---------|
| `text-embedding-3-small` | 1536 | Fast, cheap, good quality |
| `text-embedding-3-large` | 3072 | Best quality |
| `text-embedding-ada-002` | 1536 | Legacy (predecessor) |

## Simulating Embeddings for Testing

When you don't have an API key, use deterministic fake embeddings:

```python
import numpy as np
import hashlib

def fake_embedding(text: str, dims: int = 64) -> list[float]:
    """
    Generate a deterministic fake embedding for testing.
    Similar texts won't have high similarity, but structure is correct.
    """
    np.random.seed(int(hashlib.md5(text.encode()).hexdigest(), 16) % (2**32))
    vec = np.random.randn(dims)
    vec = vec / np.linalg.norm(vec)  # normalize to unit sphere
    return vec.tolist()
```

---

### Quiz

1. **Why is cosine similarity used for embeddings instead of Euclidean distance?**
2. **What is chunking and why is overlap important?**
3. **In a RAG system, what is the purpose of vector search?**

<details>
  <summary><b>Answer Key</b></summary>
  1. Cosine similarity measures the angle between vectors, not their length. Embeddings with similar meaning point in the same direction regardless of their magnitude, so cosine similarity captures semantic similarity better.
  2. Chunking splits long documents into smaller pieces that fit in context windows. Overlap (repeating some text between chunks) ensures that information near chunk boundaries isn't lost.
  3. Vector search finds the most relevant chunks from a knowledge base to include as context in the prompt, allowing the LLM to answer questions based on your specific data.
</details>

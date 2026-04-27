# Lesson 57: NumPy — The Foundation of AI Data Processing

NumPy (Numerical Python) is the bedrock of the entire Python data science and AI ecosystem. PyTorch, TensorFlow, scikit-learn, and Pandas all use NumPy arrays internally. Understanding NumPy means understanding how AI models actually work with numbers.

## Why NumPy for AI?

- **Speed**: NumPy operations run in C — 100x faster than pure Python loops
- **Vectors & Matrices**: Neural networks are fundamentally matrix operations
- **Embeddings**: AI text embeddings are NumPy arrays (or tensors)
- **Broadcasting**: Efficiently apply operations across entire datasets
- **Universal**: The standard format for passing data between AI libraries

## Installation

```bash
pip install numpy
```

## Arrays: The Core Concept

```python
import numpy as np

# 1D array — like a vector (e.g., a text embedding)
embedding = np.array([0.21, -0.84, 0.12, 0.73, -0.45])
print(f"Shape: {embedding.shape}")    # (5,)
print(f"Dtype: {embedding.dtype}")    # float64

# 2D array — like a matrix (e.g., batch of embeddings)
batch = np.array([
    [0.21, -0.84, 0.12],  # embedding for doc 1
    [0.73, -0.45, 0.88],  # embedding for doc 2
    [0.15,  0.92, -0.33]  # embedding for doc 3
])
print(f"Shape: {batch.shape}")  # (3, 3) = 3 docs, 3 dimensions
```

## Creating Arrays

```python
import numpy as np

# Zeros and ones — used to initialize neural network weights
zeros = np.zeros((3, 4))      # 3x4 matrix of zeros
ones = np.ones((2, 2))        # 2x2 matrix of ones
identity = np.eye(4)           # 4x4 identity matrix

# Range (like Python range, but returns an array)
x = np.arange(0, 10, 2)       # [0, 2, 4, 6, 8]

# Evenly spaced values — useful for plotting
linspace = np.linspace(0, 1, 5)  # [0., 0.25, 0.5, 0.75, 1.]

# Random arrays — for model initialization and testing
np.random.seed(42)
random = np.random.randn(3, 3)     # 3x3 normal distribution
uniform = np.random.uniform(0, 1, size=(100,))  # 100 values in [0,1]
```

## Indexing and Slicing

```python
import numpy as np

data = np.array([10, 20, 30, 40, 50])

print(data[0])     # 10 (first element)
print(data[-1])    # 50 (last element)
print(data[1:4])   # [20 30 40]
print(data[::2])   # [10 30 50] (every 2nd)

# 2D indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1, 2])    # 6 (row 1, col 2)
print(matrix[:, 1])    # [2, 5, 8] (all rows, column 1)
print(matrix[0, :])    # [1, 2, 3] (row 0, all columns)

# Boolean indexing — essential for filtering
scores = np.array([0.2, 0.8, 0.5, 0.9, 0.1])
high_confidence = scores[scores > 0.7]  # [0.8, 0.9]
```

## Vectorized Operations (No Loops Needed!)

```python
import numpy as np

# These operations apply to ALL elements simultaneously
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(a + b)      # [11 22 33 44 55]
print(a * 2)      # [2 4 6 8 10]
print(a ** 2)     # [1 4 9 16 25]
print(np.sqrt(a)) # [1. 1.41 1.73 2. 2.24]

# Math functions
print(np.sum(a))     # 15
print(np.mean(a))    # 3.0
print(np.std(a))     # 1.41
print(np.max(a))     # 5
print(np.argmax(a))  # 4 (index of max)
```

## AI Use Case: Cosine Similarity

Cosine similarity is how you find similar documents using embeddings:

```python
import numpy as np

def cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """
    Measure similarity between two embedding vectors.
    Returns 1.0 = identical, 0.0 = unrelated, -1.0 = opposite.
    """
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    return dot_product / (norm_a * norm_b)

# Simulated embeddings (in practice, these come from an embedding model)
doc1 = np.array([0.2, 0.8, 0.1, -0.3])  # "Python is great"
doc2 = np.array([0.3, 0.7, 0.2, -0.2])  # "Python is awesome" (similar)
doc3 = np.array([-0.8, 0.1, 0.9, 0.4])  # "The weather is sunny" (different)

print(cosine_similarity(doc1, doc2))  # ~0.99 (very similar)
print(cosine_similarity(doc1, doc3))  # ~-0.3 (different topic)
```

## AI Use Case: Softmax (Converting Logits to Probabilities)

```python
import numpy as np

def softmax(logits: np.ndarray) -> np.ndarray:
    """Convert raw model output (logits) to probabilities."""
    exp_scores = np.exp(logits - np.max(logits))  # subtract max for stability
    return exp_scores / exp_scores.sum()

# Model output for 3 classes: cat, dog, bird
logits = np.array([2.1, 0.5, -1.2])
probs = softmax(logits)
print(probs)  # [0.824, 0.152, 0.024]
print(probs.sum())  # 1.0 (always sums to 1)
```

## Reshaping Arrays

```python
import numpy as np

# Reshaping is critical when working with neural networks
flat = np.arange(12)         # [0, 1, 2, ..., 11]
matrix = flat.reshape(3, 4)  # 3x4 matrix
cube = flat.reshape(2, 2, 3) # 3D array

# Flatten back to 1D
back_to_flat = matrix.flatten()

# Adding dimensions (needed for batch processing)
vector = np.array([1, 2, 3])
batch = vector.reshape(1, -1)  # Shape (1, 3) — single sample in a batch
print(batch.shape)  # (1, 3)
```

## Broadcasting

```python
import numpy as np

# Broadcasting lets you apply operations between arrays of different shapes
matrix = np.array([[1, 2, 3], [4, 5, 6]])   # Shape (2, 3)
row_bias = np.array([10, 20, 30])             # Shape (3,)

# NumPy "broadcasts" row_bias to match matrix's shape
result = matrix + row_bias
# [[11, 22, 33],
#  [14, 25, 36]]

# Real AI use case: normalize a batch of embeddings
embeddings = np.random.randn(100, 1536)  # 100 embeddings, 1536 dims
norms = np.linalg.norm(embeddings, axis=1, keepdims=True)  # Shape (100, 1)
normalized = embeddings / norms  # Broadcasting handles the division
```

---

### Quiz

1. **What shape would a batch of 32 images (28x28 pixels, grayscale) be in NumPy?**
2. **Why is vectorized NumPy code faster than a Python for loop?**
3. **What does cosine similarity measure and why is it used for embeddings?**

<details>
  <summary><b>Answer Key</b></summary>
  1. (32, 28, 28) — 32 samples, 28 rows, 28 columns
  2. NumPy operations are implemented in C and run on contiguous memory blocks, avoiding Python's interpreter overhead for each loop iteration.
  3. Cosine similarity measures the angle between two vectors (ignoring magnitude). Embeddings with similar meaning point in similar directions, so a high cosine similarity means similar content.
</details>

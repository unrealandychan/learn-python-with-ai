"""
Lesson 57: NumPy — The Foundation of AI Data Processing
Exercise File

Run this with: python exercise.py
Requires: pip install numpy
"""

import numpy as np


# ===========================================================
# EXERCISE 1: Working with AI Embeddings
# ===========================================================
# TODO: Given these simulated text embeddings (4-dimensional vectors),
# implement cosine_similarity(a, b) and find which document is
# most similar to the query.

# Simulated embeddings from an embedding model
query = np.array([0.5, 0.8, -0.2, 0.3])
documents = {
    "Python tutorial": np.array([0.6, 0.7, -0.1, 0.4]),
    "JavaScript basics": np.array([0.4, 0.6, 0.1, 0.5]),
    "Cooking recipes": np.array([-0.8, 0.1, 0.9, -0.5]),
    "Machine learning intro": np.array([0.7, 0.9, -0.3, 0.2]),
}

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors.
    Formula: dot(a, b) / (||a|| * ||b||)
    Hint: Use np.dot() for dot product and np.linalg.norm() for magnitude.
    """
    # YOUR CODE HERE
    pass


print("=" * 50)
print("Exercise 1: Cosine Similarity for Document Search")
print("=" * 50)
similarities = {}
for doc_name, doc_embedding in documents.items():
    sim = cosine_similarity(query, doc_embedding)
    if sim is not None:
        similarities[doc_name] = sim
        print(f"  {doc_name}: {sim:.4f}")

if similarities:
    best = max(similarities, key=similarities.get)
    print(f"\nMost similar document: '{best}'")


# ===========================================================
# EXERCISE 2: Softmax — Converting Model Scores to Probabilities
# ===========================================================
# TODO: Implement softmax(logits) that converts raw model scores
# to probabilities (values between 0 and 1 that sum to 1).
# Formula: exp(x) / sum(exp(x))
# Important: subtract max(logits) before exp for numerical stability.

def softmax(logits: np.ndarray) -> np.ndarray:
    """
    Convert model logits to probability distribution.
    """
    # YOUR CODE HERE
    pass


print("\n" + "=" * 50)
print("Exercise 2: Softmax")
print("=" * 50)
# AI model output scores for classes: ["python", "javascript", "java", "c++"]
logits = np.array([3.2, 1.5, 0.8, -0.5])
probs = softmax(logits)
if probs is not None:
    labels = ["Python", "JavaScript", "Java", "C++"]
    print("Language classification probabilities:")
    for label, prob in zip(labels, probs):
        print(f"  {label}: {prob:.1%}")
    print(f"  Sum: {probs.sum():.4f} (should be 1.0)")


# ===========================================================
# EXERCISE 3: Batch Operations on Embeddings
# ===========================================================
# TODO: You have a batch of 5 text embeddings (each 6-dimensional).
# 1. Compute the L2 norm of each embedding (axis=1)
# 2. Normalize all embeddings so each has norm = 1
# 3. Compute the similarity matrix (dot product of normalized embeddings)
# 4. Find the most similar pair (highest similarity, excluding diagonal)

np.random.seed(42)
embeddings = np.random.randn(5, 6)  # 5 documents, 6 dimensions each
doc_names = ["Doc A", "Doc B", "Doc C", "Doc D", "Doc E"]

print("\n" + "=" * 50)
print("Exercise 3: Batch Embedding Operations")
print("=" * 50)

# Step 1: Compute norms
# YOUR CODE HERE: norms = ...

# Step 2: Normalize (divide each embedding by its norm)
# YOUR CODE HERE: normalized = ...

# Step 3: Compute similarity matrix using matrix multiplication
# Hint: similarity_matrix = normalized @ normalized.T
# YOUR CODE HERE: similarity_matrix = ...

# Step 4: Find most similar pair
# Hint: set diagonal to -inf first so we don't count same doc
# YOUR CODE HERE


# ===========================================================
# EXERCISE 4: Data Preprocessing for ML
# ===========================================================
# TODO: Preprocess this dataset of model performance scores.
# 1. Load the data (it's already a NumPy array)
# 2. Remove outliers (values more than 2 std devs from mean)
# 3. Normalize to [0, 1] range using min-max normalization
#    formula: (x - min) / (max - min)
# 4. Print statistics before and after

raw_scores = np.array([
    0.82, 0.79, 0.88, 0.91, 0.76, 0.85, 0.02, 0.83,
    0.78, 0.95, 0.89, 0.99, 0.81, 0.03, 0.87, 0.92
])

print("\n" + "=" * 50)
print("Exercise 4: Data Preprocessing")
print("=" * 50)

# Step 1: Print original statistics
print(f"Original: mean={raw_scores.mean():.3f}, std={raw_scores.std():.3f}, "
      f"min={raw_scores.min():.3f}, max={raw_scores.max():.3f}")

# Step 2: Remove outliers (values > 2 std devs from mean)
# YOUR CODE HERE: clean_scores = ...

# Step 3: Min-max normalize
# YOUR CODE HERE: normalized_scores = ...

# Print results
# YOUR CODE HERE


# ===========================================================
# EXERCISE 5: Matrix Operations for Neural Networks
# ===========================================================
# TODO: Simulate a single neural network layer.
# A linear layer computes: output = input @ weights + bias
# 1. Create a "weight matrix" of shape (4, 3) with random values (use np.random.seed(42))
# 2. Create a "bias vector" of shape (3,) with zeros
# 3. Create an input batch of shape (5, 4) (5 samples, 4 features)
# 4. Compute the layer output
# 5. Apply ReLU activation: relu(x) = max(0, x) — use np.maximum(0, x)
# 6. Print the output shape and values

print("\n" + "=" * 50)
print("Exercise 5: Neural Network Layer (Matrix Math)")
print("=" * 50)

np.random.seed(42)

# YOUR CODE HERE:
# weights = ...
# bias = ...
# input_batch = ...
# layer_output = ...
# activated_output = ...
# print(f"Input shape: ...")
# print(f"Output shape: ...")
# print(f"Output after ReLU:\n{...}")

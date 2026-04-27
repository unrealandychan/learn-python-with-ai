"""
Lesson 57: NumPy — Solutions
"""

import numpy as np


# ===========================================================
# SOLUTION 1: Cosine Similarity
# ===========================================================
query = np.array([0.5, 0.8, -0.2, 0.3])
documents = {
    "Python tutorial": np.array([0.6, 0.7, -0.1, 0.4]),
    "JavaScript basics": np.array([0.4, 0.6, 0.1, 0.5]),
    "Cooking recipes": np.array([-0.8, 0.1, 0.9, -0.5]),
    "Machine learning intro": np.array([0.7, 0.9, -0.3, 0.2]),
}

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)


print("=" * 50)
print("Exercise 1: Cosine Similarity for Document Search")
print("=" * 50)
similarities = {}
for doc_name, doc_embedding in documents.items():
    sim = cosine_similarity(query, doc_embedding)
    similarities[doc_name] = sim
    print(f"  {doc_name}: {sim:.4f}")

best = max(similarities, key=similarities.get)
print(f"\nMost similar document: '{best}'")


# ===========================================================
# SOLUTION 2: Softmax
# ===========================================================
def softmax(logits: np.ndarray) -> np.ndarray:
    # Subtract max for numerical stability
    shifted = logits - np.max(logits)
    exp_scores = np.exp(shifted)
    return exp_scores / exp_scores.sum()


print("\n" + "=" * 50)
print("Exercise 2: Softmax")
print("=" * 50)
logits = np.array([3.2, 1.5, 0.8, -0.5])
probs = softmax(logits)
labels = ["Python", "JavaScript", "Java", "C++"]
for label, prob in zip(labels, probs):
    print(f"  {label}: {prob:.1%}")
print(f"  Sum: {probs.sum():.4f}")


# ===========================================================
# SOLUTION 3: Batch Embedding Operations
# ===========================================================
np.random.seed(42)
embeddings = np.random.randn(5, 6)
doc_names = ["Doc A", "Doc B", "Doc C", "Doc D", "Doc E"]

print("\n" + "=" * 50)
print("Exercise 3: Batch Embedding Operations")
print("=" * 50)

# Step 1: Compute L2 norms
norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
print(f"Norms shape: {norms.shape}")

# Step 2: Normalize
normalized = embeddings / norms

# Step 3: Compute similarity matrix
similarity_matrix = normalized @ normalized.T
print(f"Similarity matrix shape: {similarity_matrix.shape}")

# Step 4: Find most similar pair (excluding diagonal)
sim_copy = similarity_matrix.copy()
np.fill_diagonal(sim_copy, -np.inf)  # exclude same-doc pairs
max_idx = np.unravel_index(np.argmax(sim_copy), sim_copy.shape)
i, j = max_idx
print(f"Most similar pair: '{doc_names[i]}' and '{doc_names[j]}' "
      f"(similarity: {similarity_matrix[i, j]:.4f})")


# ===========================================================
# SOLUTION 4: Data Preprocessing
# ===========================================================
raw_scores = np.array([
    0.82, 0.79, 0.88, 0.91, 0.76, 0.85, 0.02, 0.83,
    0.78, 0.95, 0.89, 0.99, 0.81, 0.03, 0.87, 0.92
])

print("\n" + "=" * 50)
print("Exercise 4: Data Preprocessing")
print("=" * 50)

print(f"Original: mean={raw_scores.mean():.3f}, std={raw_scores.std():.3f}, "
      f"min={raw_scores.min():.3f}, max={raw_scores.max():.3f}, n={len(raw_scores)}")

# Remove outliers
mean = raw_scores.mean()
std = raw_scores.std()
clean_scores = raw_scores[np.abs(raw_scores - mean) <= 2 * std]
print(f"After outlier removal: n={len(clean_scores)} (removed {len(raw_scores) - len(clean_scores)} outliers)")

# Min-max normalization
normalized_scores = (clean_scores - clean_scores.min()) / (clean_scores.max() - clean_scores.min())
print(f"Normalized: mean={normalized_scores.mean():.3f}, min={normalized_scores.min():.3f}, max={normalized_scores.max():.3f}")


# ===========================================================
# SOLUTION 5: Neural Network Layer
# ===========================================================
print("\n" + "=" * 50)
print("Exercise 5: Neural Network Layer (Matrix Math)")
print("=" * 50)

np.random.seed(42)

# Weights: shape (input_features=4, output_features=3)
weights = np.random.randn(4, 3)
bias = np.zeros(3)
input_batch = np.random.randn(5, 4)  # 5 samples, 4 features

# Linear transformation: output = input @ weights + bias
layer_output = input_batch @ weights + bias  # shape (5, 3)

# ReLU activation: max(0, x)
activated_output = np.maximum(0, layer_output)

print(f"Input shape:  {input_batch.shape}")
print(f"Weight shape: {weights.shape}")
print(f"Output shape: {layer_output.shape}")
print(f"\nOutput after ReLU (negatives become 0):")
print(np.round(activated_output, 3))

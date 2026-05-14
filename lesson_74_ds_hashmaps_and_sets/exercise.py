# Lesson 74: Exercise — Hash Maps & Sets Advanced Patterns
from collections import defaultdict, Counter
import re

# TODO 1: contains_nearby_duplicate(nums: list[int], k: int) -> bool
# Return True if nums[i] == nums[j] and abs(i-j) <= k
# Use a dict: {value: last_seen_index}
# # Time: O(n) | Space: O(min(n, k))

# TODO 2: subarray_sum_equals_k(nums: list[int], k: int) -> int
# Count subarrays with sum == k
# Use prefix sum: if prefix[j] - prefix[i] == k, then sum(i..j) == k
# Store {prefix_sum: count} in hash map
# # Time: O(n) | Space: O(n)

# TODO 3: word_frequency_topk(text: str, k: int) -> list[str]
# Lowercase, remove punctuation, split, count, return top k
# # Time: O(n log n) | Space: O(n)

# Test
# print(contains_nearby_duplicate([1,2,3,1], 3))   # True
# print(contains_nearby_duplicate([1,2,3,1], 2))   # False
# print(subarray_sum_equals_k([1,1,1], 2))         # 2
# print(word_frequency_topk("the cat sat on the mat the cat", 2))  # ['the', 'cat']

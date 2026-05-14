# Lesson 69: Exercise — Heap & Priority Queue
import heapq

# TODO: MedianFinder
# Two heaps:
#   self._low  — max-heap (negate values) for lower half
#   self._high — min-heap for upper half
# Invariant: len(low) == len(high) or len(low) == len(high) + 1
#
# add_num(num):
#   Always push to low first, then balance
# find_median():
#   If low longer: return -low[0]
#   Else: return (-low[0] + high[0]) / 2

# TODO: k_most_frequent(words: list[str], k: int) -> list[str]
#   Return the k most frequent words, sorted by frequency desc,
#   then alphabetically for ties

# Test MedianFinder
# mf = MedianFinder()
# for n in [1, 2, 3, 4, 5]:
#     mf.add_num(n)
#     print(mf.find_median())   # 1, 1.5, 2, 2.5, 3

# Test k_most_frequent
# print(k_most_frequent(["apple","banana","apple","cherry","banana","apple"], 2))
# # ["apple", "banana"]

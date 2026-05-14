# Lesson 74: Hash Maps & Sets (Advanced Patterns)

You already know Python dicts and sets from Lessons 10-11. This lesson covers their **internals** and **interview patterns**.

## How Hashing Works

A **hash map** (dict) maps keys to values via a **hash function**:

```
key → hash(key) → bucket index → value
```

- **Hash function:** converts key to an integer index
- **Collision handling:** two keys → same index. Python uses open addressing.
- **Load factor:** when dict is 2/3 full, Python resizes (rehashes) to maintain O(1)

```python
d = {}
d["name"] = "Alice"   # O(1) average
d["name"]             # O(1) average
"name" in d           # O(1) average
del d["name"]         # O(1) average
```

Worst case is O(n) (all keys collide), but this is rare in practice.

## Set vs Dict

```python
s = {1, 2, 3}          # Set — unique values, O(1) lookup
d = {1: "a", 2: "b"}   # Dict — key-value, O(1) lookup

1 in s    # O(1)
1 in d    # O(1)
1 in [1, 2, 3]  # O(n) — list search is linear!
```

**Always prefer set over list for membership testing.**

---

## Pattern 1: Frequency Counting

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count.most_common(2))   # [('apple', 3), ('banana', 2)]
```

## Pattern 2: Two-Sum (Classic)

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}   # {value: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
# Time: O(n) | Space: O(n)
```

## Pattern 3: Anagram Check

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
# Time: O(n) | Space: O(n)
```

## Pattern 4: Group Anagrams

```python
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))   # Canonical form
        groups[key].append(word)
    return list(groups.values())
# Time: O(n * k log k) where k = max word length | Space: O(n * k)
```

## Pattern 5: Sliding Window with Hash Map

```python
def longest_unique_substring(s: str) -> int:
    char_index = {}
    max_len = left = 0
    for right, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1
        char_index[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
# Time: O(n) | Space: O(min(n, alphabet))
```

## Pattern 6: LRU Cache (OrderedDict)

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)   # Mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Evict LRU (oldest)
```

---

## Exercise

1. Implement `contains_nearby_duplicate(nums, k) -> bool`: return True if there exist indices i, j such that `nums[i] == nums[j]` and `abs(i - j) <= k`. O(n) time.

2. Implement `subarray_sum_equals_k(nums: list[int], k: int) -> int`: count number of contiguous subarrays that sum to k. O(n) time using prefix sum + hash map.

3. Implement `word_frequency_topk(text: str, k: int) -> list[str]`: given a text string, return the k most frequent words (case-insensitive, ignore punctuation).

# Lesson 74: Solution
from collections import defaultdict, Counter, OrderedDict
import re


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    last_seen = {}
    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    return False
# Time: O(n) | Space: O(min(n, k))


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    prefix_count = defaultdict(int)
    prefix_count[0] = 1   # Empty subarray has sum 0
    prefix_sum = 0
    count = 0
    for num in nums:
        prefix_sum += num
        count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] += 1
    return count
# Time: O(n) | Space: O(n)


def word_frequency_topk(text: str, k: int) -> list[str]:
    words = re.findall(r"[a-z]+", text.lower())
    count = Counter(words)
    return [word for word, _ in count.most_common(k)]
# Time: O(n log n) | Space: O(n)


print(contains_nearby_duplicate([1, 2, 3, 1], 3))    # True
print(contains_nearby_duplicate([1, 2, 3, 1], 2))    # False
print(subarray_sum_equals_k([1, 1, 1], 2))           # 2
print(word_frequency_topk("the cat sat on the mat the cat", 2))  # ['the', 'cat']

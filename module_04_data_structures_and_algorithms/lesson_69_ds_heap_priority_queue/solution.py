# Lesson 69: Solution
import heapq
from collections import Counter


class MedianFinder:
    def __init__(self):
        self._low: list[int] = []    # max-heap (negated)
        self._high: list[int] = []   # min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self._low, -num)
        # Balance: ensure low's max <= high's min
        if self._high and -self._low[0] > self._high[0]:
            heapq.heappush(self._high, -heapq.heappop(self._low))
        # Ensure low has equal or one more element
        if len(self._low) < len(self._high):
            heapq.heappush(self._low, -heapq.heappop(self._high))
        elif len(self._low) > len(self._high) + 1:
            heapq.heappush(self._high, -heapq.heappop(self._low))

    def find_median(self) -> float:
        if len(self._low) > len(self._high):
            return float(-self._low[0])
        return (-self._low[0] + self._high[0]) / 2


def k_most_frequent(words: list[str], k: int) -> list[str]:
    count = Counter(words)
    # Sort by (-frequency, word) so heapq gives highest freq, then alpha
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]


# Test MedianFinder
mf = MedianFinder()
for n in [1, 2, 3, 4, 5]:
    mf.add_num(n)
    print(mf.find_median())    # 1.0, 1.5, 2.0, 2.5, 3.0

# Test k_most_frequent
result = k_most_frequent(["apple", "banana", "apple", "cherry", "banana", "apple"], 2)
print(result)   # ['apple', 'banana']

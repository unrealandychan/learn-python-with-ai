# Lesson 73: Sorting & Binary Search

## Why Learn Sorting?

Even though Python has `sorted()`, interviewers ask:
- What algorithm does Python use? (**Timsort** — O(n log n))
- What's the difference between merge sort and quick sort?
- Write a binary search.

---

## Merge Sort — O(n log n), Stable

Divide and conquer. Stable (preserves order of equal elements).

```python
def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]
```

**Time:** O(n log n) | **Space:** O(n)

---

## Quick Sort — O(n log n) average, O(n²) worst

In-place, not stable. Fast in practice due to cache locality.

```python
def quick_sort(arr: list, low: int = 0, high: int = None) -> None:
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

---

## Binary Search — O(log n)

Works only on **sorted** arrays. Divide search space in half each iteration.

```python
def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2   # Avoids integer overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Binary Search Variants

**Find leftmost (first occurrence):**
```python
def search_left(arr, target) -> int:
    left, right, result = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1   # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

**Search in rotated sorted array:**
```python
def search_rotated(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:   # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:                        # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

---

## Python's bisect Module

```python
import bisect

arr = [1, 3, 5, 7, 9]
bisect.bisect_left(arr, 5)    # 2 — index where 5 would be inserted (leftmost)
bisect.bisect_right(arr, 5)   # 3 — index after existing 5
bisect.insort(arr, 6)         # Insert 6 in sorted position
```

---

## Exercise

1. Implement `merge_sort(arr: list) -> list`
2. Implement `binary_search(arr: list[int], target: int) -> int`
3. Implement `search_rotated(arr: list[int], target: int) -> int`
4. Implement `find_peak(arr: list[int]) -> int` — find any peak element index (element greater than neighbours) in O(log n)

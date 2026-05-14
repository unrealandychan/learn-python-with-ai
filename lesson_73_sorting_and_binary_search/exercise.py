# Lesson 73: Exercise — Sorting & Binary Search

# TODO 1: merge_sort(arr: list) -> list
# Return a NEW sorted list using merge sort
# # Time: O(n log n) | Space: O(n)

# TODO 2: binary_search(arr: list[int], target: int) -> int
# Return index of target in sorted arr, or -1
# # Time: O(log n) | Space: O(1)

# TODO 3: search_rotated(arr: list[int], target: int) -> int
# Binary search on a rotated sorted array (no duplicates)
# e.g. [4,5,6,7,0,1,2], target=0 -> 4

# TODO 4: find_peak(arr: list[int]) -> int
# Return the index of ANY peak element (arr[i] > arr[i-1] and arr[i] > arr[i+1])
# Edge elements only need to beat one neighbour
# Must be O(log n) — use binary search!

# Test
# print(merge_sort([5,2,8,1,9,3]))           # [1,2,3,5,8,9]
# print(binary_search([1,3,5,7,9], 7))       # 3
# print(search_rotated([4,5,6,7,0,1,2], 0))  # 4
# print(find_peak([1,2,3,1]))                # 2

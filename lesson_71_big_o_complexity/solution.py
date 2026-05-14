# Lesson 71: Solution — Big-O Complexity Analysis


def has_duplicates(lst: list) -> bool:
    seen = set()
    for item in lst:          # O(n) iterations
        if item in seen:      # O(1) set lookup
            return True
        seen.add(item)        # O(1)
    return False
# Time: O(n) | Space: O(n) — worst case all unique, set holds n items


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:                     # O(n) strings
        while not s.startswith(prefix):    # O(m) where m = len(prefix)
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
# Time: O(n * m) where n = number of strings, m = length of shortest string
# Space: O(m) — stores prefix


def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:                  # O(log n) — halves search space
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Time: O(log n) | Space: O(1) — iterative, no extra memory


def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)
# Time: O(2^n) — each call branches into 2, tree depth n
# Space: O(n) — maximum call stack depth is n


def fib_iterative(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):    # O(n)
        a, b = b, a + b
    return b
# Time: O(n) | Space: O(1) — only two variables


# Quick test
print(has_duplicates([1, 2, 3, 4]))     # False
print(has_duplicates([1, 2, 3, 1]))     # True
print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
print(binary_search([1, 3, 5, 7, 9], 5))   # 2
print(fib_recursive(10))                # 55
print(fib_iterative(10))                # 55

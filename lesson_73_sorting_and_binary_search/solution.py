# Lesson 73: Solution


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]
# Time: O(n log n) | Space: O(n)


def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Time: O(log n) | Space: O(1)


def search_rotated(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:        # Left half sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:                             # Right half sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def find_peak(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1    # Peak is to the right
        else:
            right = mid       # Peak is here or to the left
    return left
# Time: O(log n) | Space: O(1)


print(merge_sort([5, 2, 8, 1, 9, 3]))           # [1, 2, 3, 5, 8, 9]
print(binary_search([1, 3, 5, 7, 9], 7))        # 3
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0)) # 4
print(find_peak([1, 2, 3, 1]))                   # 2

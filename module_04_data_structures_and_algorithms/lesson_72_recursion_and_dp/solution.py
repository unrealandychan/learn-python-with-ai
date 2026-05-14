# Lesson 72: Solution


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
# Time: O(n) | Space: O(1)


def max_subarray(nums: list[int]) -> int:
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# Time: O(n) | Space: O(1)


def word_break(s: str, word_dict: list[str]) -> bool:
    word_set = set(word_dict)    # O(1) lookup
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True                 # Empty string always valid
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
# Time: O(n^2) | Space: O(n)


print(climb_stairs(5))                              # 8
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(word_break("leetcode", ["leet", "code"]))     # True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False

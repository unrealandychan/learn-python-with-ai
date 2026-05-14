# Lesson 72: Exercise — Recursion & Dynamic Programming

# TODO 1: climb_stairs(n: int) -> int
# Count distinct ways to climb n stairs (take 1 or 2 steps)
# DP — similar to Fibonacci
# # Time: O(n) | Space: O(1) if optimised

# TODO 2: max_subarray(nums: list[int]) -> int
# Return the maximum sum contiguous subarray
# Kadane's Algorithm: track current_sum and max_sum
# # Time: O(n) | Space: O(1)

# TODO 3: word_break(s: str, word_dict: list[str]) -> bool
# Return True if s can be split into words from word_dict
# DP: dp[i] = True if s[:i] can be formed
# # Time: O(n^2 * m) | Space: O(n)

# Test
# print(climb_stairs(5))    # 8
# print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
# print(word_break("leetcode", ["leet","code"]))  # True
# print(word_break("catsandog", ["cats","dog","sand","and","cat"]))  # False

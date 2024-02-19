"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing
the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1


Dynamic Programming

[1, 2, 4, 3]

LIS[3] = 1
LIS[2] = max(1) = 1 // 4 > 3
LIS[1] = max(1, 1 + LIS[2], 1 + LIS[3]) = max(1, 2, 2) = 2
LIS[0] = max(1,1 + LIS[1], 1 + LIS[2], 1 + LIS[3]) = max(1, 3, 2, 2) = 3

O(n^2)
"""
from typing import List


def longest_increasing_subsequence(nums: List[int]):
    lis = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                lis[i] = max(lis[i], 1 + lis[j])
    return max(lis)


print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
print(longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))
print(longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))

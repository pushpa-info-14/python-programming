"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9


[100,4,200,1,3,2]

     [x][1][2][3][4][x]         [x][100][x]         [x][200][x]
----------------------------------------------------------------------
"""
from typing import List


def longest_consecutive(nums: List[int]):
    num_set = set(nums)
    longest = 0

    for n in nums:
        # check if it is the start of a sequence
        if (n - 1) not in num_set:
            length = 0
            while (n + length) in num_set:
                length += 1
            longest = max(length, longest)
    return longest


print(longest_consecutive([100, 4, 200, 1, 3, 2]))

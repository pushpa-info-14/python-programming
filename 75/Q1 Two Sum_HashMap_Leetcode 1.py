"""
Given an array of integers, return indices of the two numbers such that
they add up to specific target.

You may assume that each input would have exactly one solution, and
you may not use the same element twice.

Example:
     Given nums = [2, 7, 11, 15], target = 9,
     Because nums[0] + nums[1] = 2 + 7 = 9
     return [0, 1]
"""


def two_sum(nums, target):
    prev_map = {}  # val : index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[num] = i


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([2, 1, 5, 3], 4))

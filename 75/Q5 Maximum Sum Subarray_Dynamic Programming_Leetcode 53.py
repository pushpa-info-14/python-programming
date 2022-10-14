"""
Given an integer array nums, find the contiguous subarray (containing
at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
"""


def maximum_sum_subarray(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_sum = max(max_sum, current_sum)
    return max_sum


print(maximum_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

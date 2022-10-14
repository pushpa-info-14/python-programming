"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one
number) which has the largest product.

Example 1:
    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
"""


def maximum_product_subarray(nums):
    max_product = max(nums)
    current_min, current_max = 1, 1

    for num in nums:
        if num == 0:
            current_min, current_max = 1, 1
            continue
        temp_max = current_max * num
        current_max = max(temp_max, current_min * num, num)
        current_min = min(temp_max, current_min * num, num)
        max_product = max(max_product, current_max)
    return max_product


print(maximum_product_subarray([2, 3, -2, 4]))
print(maximum_product_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# T(n) = O(n)
# S(n) = O(1)

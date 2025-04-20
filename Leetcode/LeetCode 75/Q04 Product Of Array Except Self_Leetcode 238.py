"""
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of num is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time without using the
division operator

Example 1:
    Input: nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
Example 2:
    Input: nums = [-1, 1, 0, -3, 3]
    Output: [0, 0, 9, 0, 0]
"""


def product_except_self(nums):
    res = [1] * (len(nums))
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))

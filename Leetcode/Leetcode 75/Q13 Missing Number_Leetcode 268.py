"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
that is missing from the array.

Example 1:
    Input: nums = [3,0,1]
    Output: 2

Example 2:
    Input: nums = [0,1]
    Output: 2

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8


XOR solution
[0, 1, 2, 3] XOR [0,1,3] => 2
"""
from typing import List


def missing_number(nums):
    n = len(nums) + 1
    total_sum = int(n * (n - 1) / 2)
    current_sum = 0
    for num in nums:
        current_sum += num

    return total_sum - current_sum


def missingNumber2(nums: List[int]) -> int:
    total = 0
    expectedTotal = 0
    for i in range(len(nums)):
        total += nums[i]
        expectedTotal += i + 1

    return expectedTotal - total


def missingNumber3(nums: List[int]) -> int:
    res = len(nums)

    for i in range(len(nums)):
        res += (i - nums[i])

    return res


print(missing_number([3, 0, 1]))
print(missing_number([0, 1]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missingNumber2([3, 0, 1]))
print(missingNumber2([0, 1]))
print(missingNumber2([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missingNumber3([3, 0, 1]))
print(missingNumber3([0, 1]))
print(missingNumber3([9, 6, 4, 2, 3, 5, 7, 0, 1]))

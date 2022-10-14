"""
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
    The solution set must not contain duplicate triplets.

Example:
    Given array nums = [-1, 0, 1, 2, -1, -4]

    A solution set is:
    [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
"""


def three_sum(nums):
    res = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            summation = num + nums[left] + nums[right]
            if summation > 0:
                right -= 1
            elif summation < 0:
                left += 1
            else:
                res.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res


print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([-3, 3, 4, -3, 1, 2]))

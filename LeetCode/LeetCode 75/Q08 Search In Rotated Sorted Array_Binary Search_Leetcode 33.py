"""
Suppose an array in ascending order is rotated at some pivot unknown to you beforehand.

For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

You are given a target value to search. If found in the array return its index. Otherwise, return -1.

You may assume no duplicate exists in the array.

You must write an algorithm that runs in O(logn) time.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
"""


def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # left sorted portion
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


print(search([3, 4, 5, 1, 2], 5))
print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([1, 2, 4, 5, 6, 7, 0], 3))

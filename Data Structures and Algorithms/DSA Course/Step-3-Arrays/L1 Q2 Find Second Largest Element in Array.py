import math


def second_largest_element(nums):
    n = len(nums)
    largest = nums[0]

    for i in range(1, n):
        if nums[i] > largest:
            largest = nums[i]
    second = -1
    for i in range(n):
        if second < nums[i] < largest:
            second = nums[i]

    return second


def second_largest(nums):
    n = len(nums)
    largest = nums[0]
    s_largest = -1
    for i in range(1, n):
        if nums[i] > largest:
            s_largest = largest
            largest = nums[i]
        elif largest > nums[i] > s_largest:
            s_largest = nums[i]
    return s_largest


print(second_largest_element([1, 2, 5, 4, 7, 9]))
print(second_largest([1, 2, 5, 4, 7, 9]))

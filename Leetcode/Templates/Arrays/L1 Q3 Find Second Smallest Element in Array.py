import math


def second_smallest(nums):
    n = len(nums)
    smallest = nums[0]
    s_smallest = math.inf
    for i in range(1, n):
        if nums[i] < smallest:
            s_smallest = smallest
            smallest = nums[i]
        elif smallest < nums[i] < s_smallest:
            s_smallest = nums[i]
    return s_smallest


print(second_smallest([1, 2, 5, 4, 7, 9]))

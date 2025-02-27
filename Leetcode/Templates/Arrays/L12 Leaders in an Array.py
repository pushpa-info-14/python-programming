import math


def leaders(nums):
    n = len(nums)
    maximum = -math.inf
    res = []

    for i in range(n - 1, -1, -1):
        if nums[i] > maximum:
            res.append(nums[i])
            maximum = nums[i]
    res.sort()
    return res


# Everything to the right should be smaller
print(leaders([10, 22, 12, 3, 0, 6]))

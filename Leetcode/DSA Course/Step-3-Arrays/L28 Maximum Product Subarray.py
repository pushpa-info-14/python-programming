import math
from os import supports_fd


def maxProductBrute(nums):
    n = len(nums)
    res = -math.inf

    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= nums[k]
            res = max(res, product)
    return res


def maxProductBetter(nums):
    n = len(nums)
    res = -math.inf

    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            res = max(res, product)
    return res


def maxProductOptimal(nums):
    n = len(nums)
    res = -math.inf
    prefix = 1
    suffix = 1

    for i in range(n):
        if prefix == 0: prefix = 1
        if suffix == 0: suffix = 1

        prefix *= nums[i]
        suffix *= nums[n - i - 1]
        res = max(res, prefix, suffix)
    return res


print(maxProductBrute([2, 3, -2, 4]))  # 6
print(maxProductBetter([2, 3, -2, 4]))  # 6
print(maxProductOptimal([2, 3, -2, 4]))  # 6

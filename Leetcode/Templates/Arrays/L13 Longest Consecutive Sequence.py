import math


def lcs(nums):
    n = len(nums)
    nums.sort()
    res = 0
    count = 0
    last_smallest = -math.inf

    for i in range(n):
        if nums[i] - 1 == last_smallest:
            count += 1
            last_smallest = nums[i]
        elif nums[i] != last_smallest:
            count = 1
            last_smallest = nums[i]
        res = max(res, count)

    return res


def lcs2(nums):
    mp = set(nums)
    res = 0

    for num in mp:
        if num - 1 not in mp:
            count = 0
            n = num
            while n in mp:
                count += 1
                n += 1
            res = max(res, count)

    return res


print(lcs([102, 4, 100, 1, 101, 3, 2, 1, 1]))
print(lcs2([102, 4, 100, 1, 101, 3, 2, 1, 1]))

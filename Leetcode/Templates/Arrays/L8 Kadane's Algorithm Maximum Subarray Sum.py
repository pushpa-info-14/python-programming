import math


def max_subarray(nums):
    n = len(nums)
    res = -math.inf
    for i in range(n):
        for j in range(i, n):
            cur_sum = 0
            for k in range(i, j + 1):
                cur_sum += nums[k]
            res = max(res, cur_sum)
    return res


def max_subarray2(nums):
    n = len(nums)
    res = -math.inf
    for i in range(n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += nums[j]
            res = max(res, cur_sum)
    return res


def max_subarray3(nums):
    n = len(nums)
    res = -math.inf
    cur_sum = 0
    start = -1
    end = -1
    for i in range(n):
        if cur_sum == 0:
            start = i
        cur_sum += nums[i]

        if cur_sum > res:
            res = cur_sum
            end = i

        if cur_sum < 0:
            cur_sum = 0
    print([start, end])
    return res


print(max_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
print(max_subarray2([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
print(max_subarray3([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7

def maximum_points(nums, k):
    n = len(nums)
    l_sum = 0
    r_sum = 0

    for i in range(k):
        l_sum += nums[i]
    max_sum = l_sum

    r = n - 1
    for i in reversed(range(k)):
        l_sum -= nums[i]
        r_sum += nums[r]
        r -= 1
        max_sum = max(max_sum, l_sum + r_sum)
    return max_sum


print(maximum_points([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
def countSum(nums, k):
    n = len(nums)
    mp = {}
    cur_sum = 0
    res = 0
    mp[0] = 1
    for i in range(n):
        cur_sum += nums[i]
        rem = cur_sum - k
        if rem in mp:
            res += mp[rem]
        if cur_sum not in mp:
            mp[cur_sum] = 0
        mp[cur_sum] += 1
    return res


print(countSum([1, 2, 3, -3, 1, 1, 1, 4, 2, -3], 3))

def longest(nums, k):
    n = len(nums)
    pre_sum = {}
    cur_sum = 0
    max_len = 0

    for i in range(n):
        cur_sum += nums[i]
        if cur_sum == k:
            max_len = max(max_len, i + 1)

        rem = cur_sum - k
        if rem in pre_sum:
            max_len = max(max_len, i - pre_sum[rem])

        pre_sum[cur_sum] = i

    return max_len

def longest2(nums, k):
    n = len(nums)
    cur_sum = 0
    res = 0

    l, r = 0, 0

    while r < n:
        cur_sum += nums[r]

        while l <= r and cur_sum > k:
            cur_sum -= nums[l]
            l += 1

        if cur_sum == k:
            res = max(res, r - l + 1)
        r += 1
    return res

# This only works for positive numbers. Not 0s
# Will not work for these [2, 0, 0, 0, 3]
# Map will be replacing 2 -> 0, 2 -> 1, 2 -> 2, 2 -> 3
print(longest([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 3))
print(longest([2, 0, 0, 0, 3], 3))  # Wrong
print(longest([1, 2, 3, 0, 0, 0, 1, 1, 1, 4, 2, 3], 3))  # Wrong

# This is the optimal solution if numbers are positive and 0s
print(longest2([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 3))
print(longest2([2, 0, 0, 0, 3], 3))  # Wrong
print(longest2([1, 2, 3, 0, 0, 0, 1, 1, 1, 4, 2, 3], 3))

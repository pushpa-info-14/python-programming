def longest_subarray(nums, k):
    n = len(nums)
    l, r = 0, 0
    total = 0
    max_len = 0

    while r < n:
        total = total + nums[r]

        while total > k:
            total = total - nums[l]
            l += 1
        if total <= k:
            max_len = max(max_len, r - l + 1)
        r += 1
    return max_len


def longest_subarray2(nums, k):
    n = len(nums)
    l, r = 0, 0
    total = 0
    max_len = 0

    while r < n:
        total = total + nums[r]

        if total > k:
            total = total - nums[l]
            l += 1
        if total <= k:
            max_len = max(max_len, r - l + 1)
        r += 1
    return max_len


# 1. Constant window
# 2. Longest subarray/substring where <condition>
# 3. Number of sub-arrays where <condition>
# 4. Shortest/minimum window <condition>

print(longest_subarray([2, 5, 1, 7, 10], 14))  # O(N+N)
print(longest_subarray2([2, 5, 1, 7, 10], 14))  # O(N)
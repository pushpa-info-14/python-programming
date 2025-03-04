def longestIncreasingSubsequence(nums):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for index in range(n - 1, -1, -1):
        for prev_index in range(index - 1, -2, -1):
            length = 0 + dp[index + 1][prev_index + 1]  # Not take
            if prev_index == -1 or nums[index] > nums[prev_index]:
                length = max(length, 1 + dp[index + 1][index + 1])
            dp[index][prev_index + 1] = length

    return dp[0][-1 + 1]


def longestIncreasingSubsequenceSpaceOptimized(nums):
    n = len(nums)
    nxt = [0] * (n + 1)
    cur = [0] * (n + 1)

    for index in range(n - 1, -1, -1):
        for prev_index in range(index - 1, -2, -1):
            length = 0 + nxt[prev_index + 1]  # Not take
            if prev_index == -1 or nums[index] > nums[prev_index]:
                length = max(length, 1 + nxt[index + 1])
            cur[prev_index + 1] = length
        nxt = cur
    return cur[-1 + 1]


def longestIncreasingSubsequenceTabulation(nums):
    n = len(nums)
    dp = [1] * n
    res = 0

    for i in range(n):
        for prev in range(i):
            if nums[prev] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[prev])
        res = max(res, dp[i])
    return res


def longestIncreasingSubsequencePrint(nums):
    n = len(nums)
    dp = [1] * n
    mp = [0] * n
    cur_max = 0
    last_index = 0

    for i in range(n):
        mp[i] = i
        for prev in range(i):
            if nums[prev] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[prev])
                mp[i] = prev
        if dp[i] > cur_max:
            cur_max = dp[i]
            last_index = i

    result = [nums[last_index]]
    while mp[last_index] != last_index:
        last_index = mp[last_index]
        result.append(nums[last_index])
    return result[::-1]


# Take it
# Not take it
print(longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]))
print(longestIncreasingSubsequenceSpaceOptimized([10, 9, 2, 5, 3, 7, 101, 18]))
print(longestIncreasingSubsequenceTabulation([10, 9, 2, 5, 3, 7, 101, 18]))
print(longestIncreasingSubsequencePrint([10, 9, 2, 5, 3, 7, 101, 18]))

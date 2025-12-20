def subsetSumToK(n, k, arr):
    memo = {}

    def dfs(i, target):
        if (i, target) in memo:
            return memo[(i, target)]
        if target == 0:
            return True
        if i == 0:
            return arr[i] == target
        not_take = dfs(i - 1, target)
        take = False
        if arr[i] <= target:
            take = dfs(i - 1, target - arr[i])
        memo[(i, target)] = not_take or take
        return memo[(i, target)]

    return dfs(n - 1, k)


def subsetSumToK2(n, k, arr):
    dp = [[False] * (k + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    if arr[0] <= k:
        dp[0][arr[0]] = True
    for i in range(1, n):
        for target in range(1, k + 1):
            not_take = dp[i - 1][target]
            take = False
            if arr[i] <= target:
                take = dp[i - 1][target - arr[i]]
            dp[i][target] = not_take or take
    return dp[n - 1][k]


def subsetSumToK3(n, k, arr):
    prev = [False] * (k + 1)
    prev[0] = True
    if arr[0] <= k:
        prev[arr[0]] = True
    for i in range(1, n):
        cur = [False] * (k + 1)
        cur[0] = True
        for target in range(1, k + 1):
            not_take = prev[target]
            take = False
            if arr[i] <= target:
                take = prev[target - arr[i]]
            cur[target] = not_take or take
        prev = cur
    return prev[k]


# https://www.naukri.com/code360/problems/subset-sum-equal-to-k_1550954
print(subsetSumToK(4, 5, [4, 3, 2, 1]))
print(subsetSumToK(5, 4, [2, 5, 1, 6, 7]))
print(subsetSumToK(4, 4, [1, 1, 1, 1]))
print("-----------------------")
print(subsetSumToK2(4, 5, [4, 3, 2, 1]))
print(subsetSumToK2(5, 4, [2, 5, 1, 6, 7]))
print(subsetSumToK2(4, 4, [1, 1, 1, 1]))
print("-----------------------")
print(subsetSumToK3(4, 5, [4, 3, 2, 1]))
print(subsetSumToK3(5, 4, [2, 5, 1, 6, 7]))
print(subsetSumToK3(4, 4, [1, 1, 1, 1]))

def max_sum(nums):
    n = len(nums)
    dp = {}

    def dfs(i):
        if i == 0: return nums[0]
        if i < 0: return 0

        if i in dp:
            return dp[i]

        pick = nums[i] + dfs(i - 2)
        not_pick = dfs(i - 1)
        dp[i] = max(pick, not_pick)
        return dp[i]

    return dfs(n - 1)


def max_sum_tabulation(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n):
        pick = nums[i]
        if i > 1:
            pick += dp[i - 2]
        not_pick = dp[i - 1]
        dp[i] = max(pick, not_pick)

    return dp[n - 1]


def max_sum_tabulation2(nums):
    n = len(nums)
    prev = nums[0]
    prev2 = 0

    for i in range(1, n):
        pick = nums[i]
        if i > 1:
            pick += prev2
        not_pick = prev
        cur = max(pick, not_pick)
        prev2 = prev
        prev = cur

    return prev


print(max_sum([2, 1, 4, 9]))
print(max_sum_tabulation([2, 1, 4, 9]))
print(max_sum_tabulation2([2, 1, 4, 9]))

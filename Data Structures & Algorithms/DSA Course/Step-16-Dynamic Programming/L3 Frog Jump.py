import math


def frog_jump_momo(energy):
    n = len(energy)
    memo = {}

    def dfs(i):
        if i == 0:
            return 0
        if i in memo:
            return memo[i]
        s2 = math.inf
        s1 = dfs(i - 1) + abs(energy[i] - energy[i - 1])
        if i > 1:
            s2 = dfs(i - 2) + abs(energy[i] - energy[i - 2])
        memo[i] = min(s1, s2)
        return memo[i]

    return dfs(n - 1)


def frog_jump_tabulation(energy):
    n = len(energy)
    dp = [0] * n
    dp[0] = 0
    for i in range(1, n):
        s1 = dp[i - 1] + abs(energy[i] - energy[i - 1])
        s2 = math.inf
        if i > 1:
            s2 = dp[i - 2] + abs(energy[i] - energy[i - 2])
        dp[i] = min(s1, s2)
    return dp[n - 1]


def frog_jump_tabulation2(energy):
    n = len(energy)
    prev0 = 0
    prev1 = 0
    for i in range(1, n):
        s1 = prev1 + abs(energy[i] - energy[i - 1])
        s2 = math.inf
        if i > 1:
            s2 = prev0 + abs(energy[i] - energy[i - 2])
        cur = min(s1, s2)
        prev0 = prev1
        prev1 = cur
    return prev1


# i -> i + 1
# i -> i + 2
print(frog_jump_momo([30, 10, 60, 10, 60, 50]))
print(frog_jump_tabulation([30, 10, 60, 10, 60, 50]))
print(frog_jump_tabulation2([30, 10, 60, 10, 60, 50]))

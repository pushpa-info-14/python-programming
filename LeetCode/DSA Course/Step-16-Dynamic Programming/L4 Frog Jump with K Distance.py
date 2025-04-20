import math


def frog_jump_momo(energy, k):
    n = len(energy)
    dp = {}

    def dfs(i):
        if i == 0:
            return 0

        if i in dp:
            return dp[i]

        min_steps = math.inf
        for j in range(1, k + 1):
            if i >= j:
                jump = dfs(i - j) + abs(energy[i] - energy[i - j])
                min_steps = min(min_steps, jump)
        dp[i] = min_steps
        return dp[i]

    return dfs(n - 1)


def frog_jump_tabulation(energy, k):
    n = len(energy)
    dp = [0] * n

    dp[0] = 0

    for i in range(1, n):
        min_steps = math.inf
        for j in range(1, k + 1):
            if i >= j:
                jump = dp[i - j] + abs(energy[i] - energy[i - j])
                min_steps = min(min_steps, jump)
        dp[i] = min_steps

    return dp[n - 1]


print(frog_jump_momo([30, 10, 60, 10, 60, 50], 2))
print(frog_jump_tabulation([30, 10, 60, 10, 60, 50], 2))

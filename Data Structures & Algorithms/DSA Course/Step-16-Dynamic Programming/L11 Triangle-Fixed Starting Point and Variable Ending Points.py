def minimumPathSum(triangle, n):
    inf = 10 ** 10
    memo = {}

    def dfs(r, i):
        if (r, i) in memo:
            return memo[(r, i)]
        if r == n - 1:
            return triangle[r][i]
        if i > r:
            return inf
        res1 = triangle[r][i] + dfs(r + 1, i)
        res2 = triangle[r][i] + dfs(r + 1, i + 1)
        memo[(r, i)] = min(res1, res2)
        return memo[(r, i)]

    return dfs(0, 0)


def minimumPathSum2(triangle, n):
    inf = 10 ** 10
    dp = []
    for i in range(n):
        dp.append([inf] * (i + 1))
    dp[0][0] = triangle[0][0]
    for r in range(1, n):
        for i in range(r + 1):
            res1 = inf
            res2 = inf
            if i < r:
                res1 = triangle[r][i] + dp[r - 1][i]
            if i > 0:
                res2 = triangle[r][i] + dp[r - 1][i - 1]
            dp[r][i] = min(res1, res2)

    return min(dp[n - 1])


# https://www.naukri.com/code360/problems/triangle_1229398
print(minimumPathSum([[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]], 4))
print(minimumPathSum2([[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]], 4))

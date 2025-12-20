def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    inf = 10 ** 10
    directions = [[1, 0], [1, -1], [1, 1]]
    memo = {}

    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]
        if r == n - 1:
            return matrix[r][c]
        cur = -inf
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nc < 0 or nr == n or nc == m:
                continue
            cur = max(cur, matrix[r][c] + dfs(nr, nc))
        memo[(r, c)] = cur
        return memo[(r, c)]

    res = -inf
    for i in range(m):
        res = max(res, dfs(0, i))
    return res


def getMaxPathSum2(matrix):
    n = len(matrix)
    m = len(matrix[0])
    inf = 10 ** 10
    dp = [[-inf] * m for _ in range(n)]
    for i in range(m):
        dp[0][i] = matrix[0][i]
    for r in range(1, n):
        for c in range(m):
            res1 = matrix[r][c] + dp[r - 1][c]
            res2 = -inf
            res3 = -inf
            if c > 0:
                res2 = matrix[r][c] + dp[r - 1][c - 1]
            if c < m - 1:
                res3 = matrix[r][c] + dp[r - 1][c + 1]
            dp[r][c] = max(res1, res2, res3)
    res = -inf
    for i in range(m):
        res = max(res, dp[n - 1][i])
    return res


print(getMaxPathSum([[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]))
print(getMaxPathSum([[10, 2, 3], [3, 7, 2], [8, 1, 5]]))
print("-----------------------")
print(getMaxPathSum2([[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]))
print(getMaxPathSum2([[10, 2, 3], [3, 7, 2], [8, 1, 5]]))

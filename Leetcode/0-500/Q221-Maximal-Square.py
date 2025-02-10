from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        def dfs(r, c):
            if r == m or c == n or matrix[r][c] == "0":
                return 0
            if memo[r][c]:
                return memo[r][c]
            res = 1 + min(dfs(r + 1, c), dfs(r, c + 1), dfs(r + 1, c + 1))
            memo[r][c] = res
            return memo[r][c]

        res = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    res = max(res, dfs(r, c))
        return res * res

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        res = 0
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
                    res = max(res, dp[r][c])
        return res * res


s = Solution()
print(s.maximalSquare(
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
))
print(s.maximalSquare([["0", "1"], ["1", "0"]]))
print(s.maximalSquare([["0"]]))

print(s.maximalSquare2(
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
))
print(s.maximalSquare2([["0", "1"], ["1", "0"]]))
print(s.maximalSquare2([["0"]]))

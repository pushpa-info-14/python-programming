import math
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            if r == m or c == n or not matrix[r][c]:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]

            count = math.inf
            nei = [[r, c + 1], [r + 1, c], [r + 1, c + 1]]
            for nr, nc in nei:
                count = min(count, dfs(nr, nc))

            memo[r][c] = 1 + count
            return memo[r][c]

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    res += dfs(i, j)
        return res

    def countSquares2(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        res = 0
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if matrix[r][c]:
                    dp[r][c] = 1 + min(dp[r][c + 1], dp[r + 1][c], dp[r + 1][c + 1])
                    res += dp[r][c]

        return res


s = Solution()
print(s.countSquares([
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))
print(s.countSquares([
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]))
print(s.countSquares2([
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))
print(s.countSquares2([
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]))

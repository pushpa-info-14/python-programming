from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
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
print(s.countSquares(matrix=
[
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))
print(s.countSquares(matrix=
[
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]))

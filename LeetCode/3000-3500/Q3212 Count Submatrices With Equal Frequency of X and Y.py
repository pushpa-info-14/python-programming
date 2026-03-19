from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prefix = [[[0] * 2 for _ in range(n + 1)] for _ in range(m + 1)]
        res = 0
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                x = 1 if grid[r - 1][c - 1] == "X" else 0
                y = 1 if grid[r - 1][c - 1] == "Y" else 0
                prefix[r][c][0] = x + prefix[r - 1][c][0] + prefix[r][c - 1][0] - prefix[r - 1][c - 1][0]
                prefix[r][c][1] = y + prefix[r - 1][c][1] + prefix[r][c - 1][1] - prefix[r - 1][c - 1][1]
                if prefix[r][c][0] == prefix[r][c][1] and prefix[r][c][0] > 0:
                    res += 1
        return res


s = Solution()
print(s.numberOfSubmatrices(grid=[["X", "Y", "."], ["Y", ".", "."]]))
print(s.numberOfSubmatrices(grid=[["X", "X"], ["X", "Y"]]))
print(s.numberOfSubmatrices(grid=[[".", "."], [".", "."]]))

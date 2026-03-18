from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                prefix[r][c] = grid[r - 1][c - 1] + prefix[r - 1][c] + prefix[r][c - 1] - prefix[r - 1][c - 1]
                if prefix[r][c] <= k:
                    res += 1
        return res


s = Solution()
print(s.countSubmatrices(grid=[[7, 6, 3], [6, 6, 1]], k=18))
print(s.countSubmatrices(grid=[[7, 2, 9], [1, 5, 0], [2, 6, 6]], k=20))

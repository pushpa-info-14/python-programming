from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m = len(grid)
        n = len(grid[0])
        p_prod = [1] * (m * n + 1)
        s_prod = [1] * (m * n + 1)
        for r in range(m):
            for c in range(n):
                i = r * n + c
                p_prod[i + 1] = (p_prod[i] * grid[r][c]) % mod
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                i = r * n + c
                s_prod[i] = (s_prod[i + 1] * grid[r][c]) % mod
        for r in range(m):
            for c in range(n):
                i = r * n + c
                grid[r][c] = (p_prod[i] * s_prod[i + 1]) % mod
        return grid


s = Solution()
print(s.constructProductMatrix(grid=[[1, 2], [3, 4]]))
print(s.constructProductMatrix(grid=[[12345], [2], [1]]))

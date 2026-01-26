from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for r in range(1, m):
            for c in range(n):
                if grid[r - 1][c] >= grid[r][c]:
                    res += grid[r - 1][c] - grid[r][c] + 1
                    grid[r][c] = grid[r - 1][c] + 1
        return res


s = Solution()
print(s.minimumOperations(grid=[[3, 2], [1, 3], [3, 4], [0, 1]]))
print(s.minimumOperations(grid=[[3, 2, 1], [2, 1, 0], [1, 2, 3]]))

from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if c > 0:
                    if grid[r][c - 1] == grid[r][c]:
                        return False
                if r > 0:
                    if grid[r - 1][c] != grid[r][c]:
                        return False
        return True


s = Solution()
print(s.satisfiesConditions(grid=[[1, 0, 2], [1, 0, 2]]))
print(s.satisfiesConditions(grid=[[1, 1, 1], [0, 0, 0]]))
print(s.satisfiesConditions(grid=[[1], [2], [3]]))

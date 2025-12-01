from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        xy = 0
        xz = [0] * m
        yz = [0] * n
        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                if x:
                    xy += 1
                xz[i] = max(xz[i], x)
                yz[j] = max(yz[j], x)
        return xy + sum(xz) + sum(yz)


s = Solution()
print(s.projectionArea(grid=[[1, 2], [3, 4]]))
print(s.projectionArea(grid=[[2]]))
print(s.projectionArea(grid=[[1, 0], [0, 2]]))

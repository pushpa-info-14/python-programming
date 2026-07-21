from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m * n
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rc = j + k
                r = (i + (rc // n)) % m
                c = rc % n
                res[r][c] = grid[i][j]
        return res


s = Solution()
print(s.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
print(s.shiftGrid(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4))
print(s.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=9))

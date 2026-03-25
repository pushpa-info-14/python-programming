from itertools import accumulate
from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                pre_sum[r + 1][c + 1] = grid[r][c] + pre_sum[r + 1][c] + pre_sum[r][c + 1] - pre_sum[r][c]
        for r in range(1, m + 1):
            if pre_sum[r][-1] == pre_sum[-1][-1] - pre_sum[r][-1]:
                return True
        for c in range(1, n + 1):
            if pre_sum[-1][c] == pre_sum[-1][-1] - pre_sum[-1][c]:
                return True
        return False

    def canPartitionGrid2(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        row_sums = [0] * m
        col_sums = [0] * n
        total = 0
        for r in range(m):
            for c in range(n):
                row_sums[r] += grid[r][c]
                col_sums[c] += grid[r][c]
                total += grid[r][c]

        return any(
            s == total / 2
            for sums in (row_sums, col_sums)
            for s in accumulate(sums)
        )

    def canPartitionGrid3(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total = 0
        for r in range(m):
            for c in range(n):
                total += grid[r][c]
        cur = 0
        for r in range(m):
            for c in range(n):
                cur += grid[r][c]
            if total / 2 == cur:
                return True
        cur = 0
        for c in range(n):
            for r in range(m):
                cur += grid[r][c]
            if total / 2 == cur:
                return True
        return False


s = Solution()
print(s.canPartitionGrid(grid=[[1, 4], [2, 3]]))
print(s.canPartitionGrid(grid=[[1, 3], [2, 4]]))
print("----------")
print(s.canPartitionGrid2(grid=[[1, 4], [2, 3]]))
print(s.canPartitionGrid2(grid=[[1, 3], [2, 4]]))
print("----------")
print(s.canPartitionGrid3(grid=[[1, 4], [2, 3]]))
print(s.canPartitionGrid3(grid=[[1, 3], [2, 4]]))

from itertools import pairwise
from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for r in range(m - k + 1):
            for c in range(n - k + 1):
                unique_nums = set()
                for nr in range(r, r + k):
                    for nc in range(c, c + k):
                        unique_nums.add(grid[nr][nc])
                if len(unique_nums) == 1:
                    continue
                res[r][c] = min(b - a for a, b in pairwise(sorted(unique_nums)))
        return res


s = Solution()
print(s.minAbsDiff(grid=[[1, 8], [3, -2]], k=2))
print(s.minAbsDiff(grid=[[3, -1]], k=1))
print(s.minAbsDiff(grid=[[1, -2, 3], [2, 3, 5]], k=2))

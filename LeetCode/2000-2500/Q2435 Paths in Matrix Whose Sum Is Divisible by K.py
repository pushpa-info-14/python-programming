from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])

        @cache
        def dfs(r, c, rem):
            if r >= m or c >= n:
                return 0
            rem = (rem + grid[r][c]) % k
            if r == m - 1 and c == n - 1 and rem == 0:
                return 1

            return (dfs(r + 1, c, rem) + dfs(r, c + 1, rem)) % mod

        res = dfs(0, 0, 0)
        dfs.cache_clear()
        return res

    def numberOfPaths2(self, grid: List[List[int]], k: int) -> int:
        mod = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])

        prev = [defaultdict(int) for _ in range(n)]
        prev[0][grid[0][0] % k] = 1
        for c in range(1, n):
            for key, value in prev[c - 1].items():
                x = (key + grid[0][c]) % k
                prev[c][x] += value

        for r in range(1, m):
            cur = [defaultdict(int) for _ in range(n)]
            for c in range(n):
                for key, value in prev[c].items():
                    x = (key + grid[r][c]) % k
                    cur[c][x] = value
                if c > 0:
                    for key, value in cur[c - 1].items():
                        x = (key + grid[r][c]) % k
                        cur[c][x] += value
            prev = cur

        return prev[-1][0] % mod


s = Solution()
print(s.numberOfPaths(grid=[[5, 2, 4], [3, 0, 5], [0, 7, 2]], k=3))
print(s.numberOfPaths(grid=[[0, 0]], k=5))
print(s.numberOfPaths(grid=[[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], k=1))
print(s.numberOfPaths2(grid=[[5, 2, 4], [3, 0, 5], [0, 7, 2]], k=3))
print(s.numberOfPaths2(grid=[[0, 0]], k=5))
print(s.numberOfPaths2(grid=[[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], k=1))

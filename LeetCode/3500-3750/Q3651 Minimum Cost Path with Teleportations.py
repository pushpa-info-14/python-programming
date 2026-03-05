from functools import cache
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        inf = 10 ** 10
        cost = [[inf] * n for _ in range(m)]  # const[i][j] = minimum cost to reach destination from (i, j)
        cost[-1][-1] = 0
        t_cost = [inf] * (max(max(row) for row in grid) + 1)
        for t in range(k + 1):
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    # Move right, down, or teleport
                    if i < m - 1:
                        cost[i][j] = min(cost[i][j], cost[i + 1][j] + grid[i + 1][j])
                    if j < n - 1:
                        cost[i][j] = min(cost[i][j], cost[i][j + 1] + grid[i][j + 1])
                    cost[i][j] = min(cost[i][j], t_cost[grid[i][j]])
            # Compute t_cost for next t
            for i in range(m):
                for j in range(n):
                    t_cost[grid[i][j]] = min(t_cost[grid[i][j]], cost[i][j])
            # Compute prefix min
            for i in range(1, len(t_cost)):
                t_cost[i] = min(t_cost[i], t_cost[i - 1])
        return cost[0][0]

    def minCost2(self, grid: List[List[int]], k: int) -> int:
        inf = 10 ** 10
        m = len(grid)
        n = len(grid[0])
        dirs = [[0, 1], [1, 0]]

        @cache
        def dfs(r, c, t):
            if r == m - 1 and c == n - 1:
                return 0
            cur = inf
            # Move down and right
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if nr == m or nc == n:
                    continue
                cur = min(cur, grid[nr][nc] + dfs(nr, nc, t))
            # Teleport
            if t > 0:
                for x in range(m):
                    for y in range(n):
                        if grid[x][y] <= grid[r][c]:
                            cur = min(cur, dfs(x, y, t - 1))
            return cur

        return dfs(0, 0, k)


s = Solution()
print(s.minCost(grid=[[1, 3, 3], [2, 5, 4], [4, 3, 5]], k=2))
print(s.minCost(grid=[[1, 2], [2, 3], [3, 4]], k=1))
print(s.minCost(grid=[[6, 7, 1, 20, 11], [4, 5, 18, 23, 28]], k=3))
print("--------------------")
# Not optimal. TLE.
print(s.minCost2(grid=[[1, 3, 3], [2, 5, 4], [4, 3, 5]], k=2))
print(s.minCost2(grid=[[1, 2], [2, 3], [3, 4]], k=1))
print(s.minCost2(grid=[[6, 7, 1, 20, 11], [4, 5, 18, 23, 28]], k=3))

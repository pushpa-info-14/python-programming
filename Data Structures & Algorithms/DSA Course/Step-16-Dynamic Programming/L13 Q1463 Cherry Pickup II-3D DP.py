from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        inf = 10 ** 10
        directions = [-1, 0, 1]

        @cache
        def dfs(r, c1, c2):
            if r < 0 or c1 < 0 or c2 < 0 or c1 == cols or c2 == cols:
                return -inf
            if r == rows - 1:
                if c1 != c2:
                    return grid[r][c1] + grid[r][c2]
                else:
                    return grid[r][c1]
            cur = -inf
            if c1 != c2:
                value = grid[r][c1] + grid[r][c2]
            else:
                value = grid[r][c1]
            for dc1 in directions:
                for dc2 in directions:
                    nc1 = c1 + dc1
                    nc2 = c2 + dc2
                    cur = max(cur, value + dfs(r + 1, nc1, nc2))
            return cur

        return dfs(0, 0, cols - 1)

    def cherryPickup2(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        inf = 10 ** 10
        directions = [-1, 0, 1]
        dp = [[[-inf for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]
        for c1 in range(cols):
            for c2 in range(cols):
                if c1 != c2:
                    dp[rows - 1][c1][c2] = grid[rows - 1][c1] + grid[rows - 1][c2]
                else:
                    dp[rows - 1][c1][c2] = grid[rows - 1][c1]
        for r in range(rows - 2, -1, -1):
            for c1 in range(cols):
                for c2 in range(cols):
                    cur = -inf
                    if c1 != c2:
                        value = grid[r][c1] + grid[r][c2]
                    else:
                        value = grid[r][c1]
                    for dc1 in directions:
                        for dc2 in directions:
                            nc1 = c1 + dc1
                            nc2 = c2 + dc2
                            if nc1 < 0 or nc2 < 0 or nc1 == cols or nc2 == cols:
                                continue
                            cur = max(cur, value + dp[r + 1][nc1][nc2])
                    dp[r][c1][c2] = cur
        return dp[0][0][cols - 1]


s = Solution()
print(s.cherryPickup(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
print(s.cherryPickup(grid=[[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                           [1, 0, 2, 3, 0, 0, 6]]))
print("-----------------------------------------")
print(s.cherryPickup2(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
print(s.cherryPickup2(grid=[[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                            [1, 0, 2, 3, 0, 0, 6]]))

from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            res = grid[r][c]
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                res += dfs(nr, nc)
            return res

        visited = set()
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (r, c) not in visited:
                    res = max(res, dfs(r, c))
        return res


s = Solution()
print(s.findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
print(s.findMaxFish([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))
print(s.findMaxFish([[6, 1, 10]]))

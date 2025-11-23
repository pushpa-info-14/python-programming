from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def is_out_of_bounds(r, c):
            return r < 0 or c < 0 or r == n or c == n

        def dfs(r, c, label):
            if is_out_of_bounds(r, c) or grid[r][c] != 1:
                return 0
            grid[r][c] = label
            size = 1
            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in nei:
                size += dfs(nr, nc, label)
            return size

        def connect(r, c):
            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            visited = set()
            res = 1
            for nr, nc in nei:
                if not is_out_of_bounds(nr, nc) and grid[nr][nc] not in visited:
                    res += size[grid[nr][nc]]
                    visited.add(grid[nr][nc])
            return res

        # 1. Pre-calculate areas
        size = defaultdict(int)  # island label -> size
        label = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size[label] = dfs(r, c, label)
                    label += 1

        # 2. Try flipping water
        res = 0 if not size else max(size.values())
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    res = max(res, connect(r, c))
        return res


s = Solution()
print(s.largestIsland([[1, 0], [0, 1]]))
print(s.largestIsland([[1, 1], [1, 0]]))
print(s.largestIsland([[1, 1], [1, 1]]))

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        directions = [-1, 0, 1, 0, -1]
        island_count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == "0" or visited[r][c]:
                return 0
            visited[r][c] = True
            for i in range(4):
                nr = r + directions[i]
                nc = c + directions[i + 1]
                dfs(nr, nc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    island_count += 1

        return island_count


s = Solution()
print(s.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))

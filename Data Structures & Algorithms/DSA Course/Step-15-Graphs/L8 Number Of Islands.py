from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            visited[r][c] = True
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr == m or nc == n or visited[nr][nc] or grid[nr][nc] == '0':
                    continue
                dfs(nr, nc)

        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res


# LeetCode 200
s = Solution()
print(s.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(s.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))

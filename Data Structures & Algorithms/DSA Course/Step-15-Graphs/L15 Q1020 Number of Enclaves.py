from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = 0

        def dfs(r, c):
            visited[r][c] = 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc] or grid[nr][nc] == 0:
                    continue
                dfs(nr, nc)

        for row in range(m):
            if grid[row][0] == 1:
                dfs(row, 0)
            if grid[row][n - 1] == 1:
                dfs(row, n - 1)
        for col in range(n):
            if grid[0][col] == 1:
                dfs(0, col)
            if grid[m - 1][col] == 1:
                dfs(m - 1, col)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    res += 1

        return res


s = Solution()
print(s.numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(s.numEnclaves(grid=[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))

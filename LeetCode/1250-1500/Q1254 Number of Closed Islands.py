class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def explore(r, c):
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc] or grid[nr][nc] == 1:
                    continue
                explore(nr, nc)

        for i in range(m):
            if not visited[i][0] and grid[i][0] == 0:
                explore(i, 0)
            if not visited[i][n - 1] and grid[i][n - 1] == 0:
                explore(i, n - 1)
        for j in range(n):
            if not visited[0][j] and grid[0][j] == 0:
                explore(0, j)
            if not visited[m - 1][j] and grid[m - 1][j] == 0:
                explore(m - 1, j)
        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 0:
                    explore(i, j)
                    res += 1
        return res


s = Solution()
print(s.closedIsland(
    grid=[[1, 1, 1, 1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 1, 1, 0],
          [1, 0, 1, 0, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 0]]))
print(s.closedIsland(grid=[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
print(s.closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1],
                           [1, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 1, 1, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 1, 1, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 1],
                           [1, 1, 1, 1, 1, 1, 1]]))

from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c):
            if (r, c) == (m - 1, n - 1):
                return True
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc]:
                    continue
                value = grid[r][c]
                if value == 1:
                    if (nc == c - 1 and grid[nr][nc] in (1, 4, 6)) or (nc == c + 1 and grid[nr][nc] in (1, 3, 5)):
                        if dfs(nr, nc):
                            return True
                elif value == 2:
                    if (nr == r - 1 and grid[nr][nc] in (2, 3, 4)) or (nr == r + 1 and grid[nr][nc] in (2, 5, 6)):
                        if dfs(nr, nc):
                            return True
                elif value == 3:
                    if (nc == c - 1 and grid[nr][nc] in (1, 4, 6)) or (nr == r + 1 and grid[nr][nc] in (2, 5, 6)):
                        if dfs(nr, nc):
                            return True
                elif value == 4:
                    if (nc == c + 1 and grid[nr][nc] in (1, 3, 5)) or (nr == r + 1 and grid[nr][nc] in (2, 5, 6)):
                        if dfs(nr, nc):
                            return True
                elif value == 5:
                    if (nc == c - 1 and grid[nr][nc] in (1, 4, 6)) or (nr == r - 1 and grid[nr][nc] in (2, 3, 4)):
                        if dfs(nr, nc):
                            return True
                elif value == 6:
                    if (nc == c + 1 and grid[nr][nc] in (1, 3, 5)) or (nr == r - 1 and grid[nr][nc] in (2, 3, 4)):
                        if dfs(nr, nc):
                            return True
            return False

        return dfs(0, 0)


s = Solution()
print(s.hasValidPath(grid=[[2, 4, 3], [6, 5, 2]]))
print(s.hasValidPath(grid=[[1, 2, 1], [1, 2, 1]]))
print(s.hasValidPath(grid=[[1, 1, 2]]))

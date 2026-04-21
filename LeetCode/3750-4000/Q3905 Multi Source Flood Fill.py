from collections import deque


class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque()
        for r, c, color in sources:
            q.append((r, c, color))
            grid[r][c] = color
            visited[r][c] = True

        while q:
            cells = set()
            for _ in range(len(q)):
                r, c, color = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr == n or nc < 0 or nc == m or visited[nr][nc]:
                        continue
                    grid[nr][nc] = max(grid[nr][nc], color)
                    cells.add((nr, nc))
            for r, c in cells:
                visited[r][c] = True
                q.append((r, c, grid[r][c]))
        return grid


s = Solution()
print(s.colorGrid(n=3, m=3, sources=[[0, 0, 1], [2, 2, 2]]))
print(s.colorGrid(n=3, m=3, sources=[[0, 1, 3], [1, 1, 5]]))
print(s.colorGrid(n=2, m=2, sources=[[1, 1, 5]]))
print(s.colorGrid(n=316, m=316, sources=[[0, 0, 777]]))

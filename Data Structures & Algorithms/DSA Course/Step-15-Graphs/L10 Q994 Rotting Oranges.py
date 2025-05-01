from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        visited = [[False] * n for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        q = deque()
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited[i][j] = True
                elif grid[i][j] == 1:
                    fresh_count += 1

        while q and fresh_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc] or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    grid[nr][nc] = 2
                    fresh_count -= 1
            res += 1

        return res if fresh_count == 0 else -1


s = Solution()
print(s.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(s.orangesRotting(grid=[[0, 2]]))

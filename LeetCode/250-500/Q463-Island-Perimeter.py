from collections import deque
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    q.append([i, j])
                    visited[i][j] = True
                    res = 0
                    while q:
                        r, c = q.popleft()
                        nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                        for nr, nc in nei:
                            if nr < 0 or nc < 0 or nr == m or nc == n or grid[nr][nc] == 0:
                                res += 1
                                continue
                            if visited[nr][nc]:
                                continue
                            q.append([nr, nc])
                            visited[nr][nc] = True
                    return res

    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0:
                return 1
            if visited[r][c]:
                return 0
            visited[r][c] = True

            res = 0
            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in nei:
                res += dfs(nr, nc)
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i, j)


s = Solution()
print(s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(s.islandPerimeter([[1]]))
print(s.islandPerimeter([[1, 0]]))

print(s.islandPerimeter2([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(s.islandPerimeter2([[1]]))
print(s.islandPerimeter2([[1, 0]]))

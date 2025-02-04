from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[0] * n for _ in range(m)]
        q = deque()

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0 or visited[r][c]:
                return 0
            q.append([r, c])
            visited[r][c] = 1
            res = 1
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            return res

        def bfs():
            min_flips = 0
            while q:
                length = len(q)
                for _ in range(length):
                    r, c = q.popleft()

                    for idx in range(4):
                        nr = r + directions[idx][0]
                        nc = c + directions[idx][1]

                        if nr < 0 or nc < 0 or nr == m or nc == n or visited[nr][nc]:
                            continue
                        if grid[nr][nc]:
                            return min_flips
                        else:
                            q.append([nr, nc])
                            visited[nr][nc] = 1
                min_flips += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    dfs(i, j)
                    return bfs()


s = Solution()
print(s.shortestBridge([[0, 1], [1, 0]]))
print(s.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
print(s.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))

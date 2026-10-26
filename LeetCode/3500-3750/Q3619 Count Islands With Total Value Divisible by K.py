from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = [[False] * n for _ in range(m)]

        def explore(r, c):
            visited[r][c] = True
            cur = grid[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc] or grid[nr][nc] == 0:
                    continue
                cur += explore(nr, nc)
            return cur

        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] > 0:
                    if explore(i, j) % k == 0:
                        res += 1
        return res


s = Solution()
print(s.countIslands(grid=[[0, 2, 1, 0, 0], [0, 5, 0, 0, 5], [0, 0, 1, 0, 0], [0, 1, 4, 7, 0], [0, 2, 0, 0, 8]], k=5))
print(s.countIslands(grid=[[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], k=3))
print(s.countIslands(grid=[[0, 0, 0], [0, 0, 1], [11, 0, 6], [0, 10, 2], [0, 0, 0], [8, 0, 0]], k=19))

from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c, lr, lc, color):
            if visited[r][c]:
                return True
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] != color or (nr, nc) == (lr, lc):
                    continue
                if dfs(nr, nc, r, c, color):
                    return True
            return False

        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if dfs(i, j, -1, -1, grid[i][j]):
                    return True
        return False


s = Solution()
print(s.containsCycle(grid=[["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]))
print(s.containsCycle(grid=[["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]))
print(s.containsCycle(grid=[["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]))

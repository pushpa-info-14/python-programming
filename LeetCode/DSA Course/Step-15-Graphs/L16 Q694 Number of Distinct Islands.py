from typing import List


class Solution:
    def distinctIslands(self, arr: List[List[int]]) -> int:
        n = len(arr)
        m = len(arr[0])
        visited = [[0] * m for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c, coordinates, r0, c0):
            visited[r][c] = 1
            coordinates.append((r - r0, c - c0))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == n or nc < 0 or nc == m or visited[nr][nc] or arr[nr][nc] == 0:
                    continue
                dfs(nr, nc, coordinates, r0, c0)

        unique = set()
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and arr[i][j] == 1:
                    co = []
                    dfs(i, j, co, i, j)
                    co.sort()
                    unique.add(tuple(co))

        return len(unique)


s = Solution()
print(s.distinctIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))  # 1
print(s.distinctIslands([[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]))  # 3

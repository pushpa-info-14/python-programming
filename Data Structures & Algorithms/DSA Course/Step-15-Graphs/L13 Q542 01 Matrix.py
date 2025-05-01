from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [mat[r].copy() for r in range(m)]
        visited = [[0] * n for _ in range(m)]
        q = deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited[i][j] = 1

        while q:
            for _ in range(len(q)):
                r, c, distance = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc]:
                        continue
                    q.append((nr, nc, distance + 1))
                    visited[nr][nc] = 1
                    res[nr][nc] = distance + 1

        return res


s = Solution()
print(s.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))

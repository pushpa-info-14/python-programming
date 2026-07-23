import heapq
from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[0] * n for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    visited.add((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == n or nc < 0 or nc == n or (nr, nc) in visited:
                    continue
                q.append((nr, nc))
                dist[nr][nc] = dist[r][c] + 1
                visited.add((nr, nc))

        res = dist[0][0]
        visited = {(0, 0)}
        q = [(-dist[0][0], 0, 0)]
        while q:
            d, r, c = heapq.heappop(q)
            res = min(res, -d)
            if (r, c) == (n - 1, n - 1):
                break
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == n or nc < 0 or nc == n or (nr, nc) in visited:
                    continue
                heapq.heappush(q, (-dist[nr][nc], nr, nc))
                visited.add((nr, nc))
        return res


s = Solution()
print(s.maximumSafenessFactor(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
print(s.maximumSafenessFactor(grid=[[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
print(s.maximumSafenessFactor(grid=[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]))
print(s.maximumSafenessFactor(grid=[[0,0],[0,1]]))

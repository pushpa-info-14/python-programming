import heapq
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        if grid[0][0] == 1:
            health -= 1
        q = [(-health, 0, 0)]  # health, r, c
        visited = set()
        visited.add((0, 0))
        while q:
            cur, r, c = heapq.heappop(q)
            cur = -cur
            if cur == 0:
                continue
            if (r, c) == (m - 1, n - 1):
                return True
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n or (nr, nc) in visited:
                    continue
                if grid[nr][nc] == 1:
                    heapq.heappush(q, (-(cur - 1), nr, nc))
                else:
                    heapq.heappush(q, (-cur, nr, nc))
                visited.add((nr, nc))
        return False


s = Solution()
print(s.findSafeWalk(grid=[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], health=1))
print(s.findSafeWalk(grid=[[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]], health=3))
print(s.findSafeWalk(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], health=5))
print(s.findSafeWalk(grid=[[1, 1, 1, 1]], health=4))

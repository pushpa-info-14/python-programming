import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [(grid[0][0], 0, 0)]  # t, x, y
        visited = [[False] * n for _ in range(n)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            t, x, y = heapq.heappop(q)
            if (x, y) == (n - 1, n - 1):
                return t
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_y < 0 or new_x == n or new_y == n or visited[new_x][new_y]:
                    continue
                visited[new_x][new_y] = True
                heapq.heappush(q, (max(t, grid[new_x][new_y]), new_x, new_y))
        return 0


s = Solution()
print(s.swimInWater(grid=[[0, 2], [1, 3]]))
print(s.swimInWater(
    grid=[[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))

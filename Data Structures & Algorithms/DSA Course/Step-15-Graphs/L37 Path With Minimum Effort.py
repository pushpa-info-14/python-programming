import heapq
from typing import List


class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        int_max = 10 ** 9
        distance = [[int_max] * columns for _ in range(rows)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = [(0, 0, 0)]  # (distance, row, col)
        distance[0][0] = 0

        while q:
            d, r, c = heapq.heappop(q)
            if r == rows - 1 and c == columns - 1:
                return d
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == rows or nc < 0 or nc == columns:
                    continue
                abs_diff = abs(heights[nr][nc] - heights[r][c])
                max_abs_diff = max(d, abs_diff)
                if distance[nr][nc] > max_abs_diff:
                    distance[nr][nc] = max_abs_diff
                    heapq.heappush(q, (distance[nr][nc], nr, nc))
        return 0


s = Solution()
print(s.MinimumEffort(rows=3, columns=3, heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(s.MinimumEffort(rows=2, columns=2, heights=[[7, 7], [7, 7]]))

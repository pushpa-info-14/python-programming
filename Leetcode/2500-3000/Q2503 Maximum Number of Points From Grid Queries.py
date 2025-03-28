from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        min_heap = [(grid[0][0], 0, 0)]  # val, r, c
        res = [0] * len(queries)
        points = 0
        visited = {(0, 0)}

        for limit, index in q:
            while min_heap and min_heap[0][0] < limit:
                val, r, c = heappop(min_heap)
                points += 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr == m or nc < 0 or nc == n or (nr, nc) in visited:
                        continue
                    heappush(min_heap, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
            res[index] = points
        return res


s = Solution()
print(s.maxPoints(grid=[[1, 2, 3], [2, 5, 7], [3, 5, 1]], queries=[5, 6, 2]))
print(s.maxPoints(grid=[[5, 2, 1], [1, 1, 2]], queries=[3]))

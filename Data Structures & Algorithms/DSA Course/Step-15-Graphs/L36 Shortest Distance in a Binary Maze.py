import heapq
from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if not grid[source[0]][source[1]] or not grid[destination[0]][destination[1]]:
            return -1

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[False] * cols for _ in range(rows)]
        q = deque()
        q.append((0, source[0], source[1]))
        visited[source[0]][source[1]] = True

        while q:
            d, r, c = q.popleft()
            if r == destination[0] and c == destination[1]:
                return d
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] == 0 or visited[nr][nc]:
                    continue
                q.append((d + 1, nr, nc))
                visited[nr][nc] = True
        return -1

    def shortestPath2(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if not grid[source[0]][source[1]] or not grid[destination[0]][destination[1]]:
            return -1

        int_max = 10**9
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        distance = [[int_max] * cols for _ in range(rows)]
        q = deque()
        q.append((0, source[0], source[1]))
        distance[source[0]][source[1]] = 0

        while q:
            d, r, c = q.popleft()
            if r == destination[0] and c == destination[1]:
                return d
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] == 0:
                    continue
                if distance[nr][nc] > d + 1:
                    q.append((d + 1, nr, nc))
                    distance[nr][nc] = d + 1
        return -1

# No need to have a priority queue due to unit weights
s = Solution()
print(s.shortestPath(grid=[[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 0, 1]],
                     source=[0, 1],
                     destination=[2, 2]))
print(s.shortestPath(grid=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 0, 1, 0, 1]],
                     source=[0, 0],
                     destination=[3, 4]))
print(s.shortestPath2(grid=[[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 0, 1]],
                     source=[0, 1],
                     destination=[2, 2]))
print(s.shortestPath2(grid=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 0, 1, 0, 1]],
                     source=[0, 0],
                     destination=[3, 4]))

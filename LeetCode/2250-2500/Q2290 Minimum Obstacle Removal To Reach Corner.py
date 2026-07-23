import heapq
from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque([(0, 0, 0)])  # (obstacles, r, c)
        visited = {(0, 0)}

        while q:
            obstacles, r, c = q.popleft()

            if (r, c) == (m - 1, n - 1):
                return obstacles
            for i in range(4):
                newR = r + directions[i][0]
                newC = c + directions[i][1]

                if (newR, newC) in visited or newR < 0 or newC < 0 or newR == m or newC == n:
                    continue
                if grid[newR][newC]:
                    q.append((obstacles + 1, newR, newC))
                else:
                    q.appendleft((obstacles, newR, newC))
                visited.add((newR, newC))

    def minimumObstacles2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = [(0, 0, 0)]  # (obstacles, r, c)
        visited = {(0, 0)}

        while q:
            obstacles, r, c = heapq.heappop(q)

            if (r, c) == (m - 1, n - 1):
                return obstacles
            for i in range(4):
                newR = r + directions[i][0]
                newC = c + directions[i][1]

                if (newR, newC) in visited or newR < 0 or newC < 0 or newR == m or newC == n:
                    continue
                heapq.heappush(q, (obstacles + grid[newR][newC], newR, newC))
                visited.add((newR, newC))


solution = Solution()
print(solution.minimumObstacles([[0, 1, 1], [1, 1, 0], [1, 1, 0]]))  # 2
print(solution.minimumObstacles([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]))  # 0
print(solution.minimumObstacles2([[0, 1, 1], [1, 1, 0], [1, 1, 0]]))  # 2
print(solution.minimumObstacles2([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]))  # 0

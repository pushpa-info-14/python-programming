import heapq
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = [(0, 0, 0)]  # cost, x, y
        visited = {(0, 0)}

        while q:
            cost, x, y = heapq.heappop(q)

            if (x, y) == (m - 1, n - 1):
                return cost

            for i in range(4):
                newX = x + directions[i][0]
                newY = y + directions[i][1]

                if newX < 0 or newY < 0 or newX == m or newY == n or (newX, newY) in visited:
                    continue
                wait = 0
                if abs(grid[newX][newY] - cost) % 2 == 0:
                    wait = 1
                newCost = max(grid[newX][newY] + wait, cost + 1)
                heapq.heappush(q, (newCost, newX, newY))
                visited.add((newX, newY))


# diff = 0 nextTime + 1
# diff = 1 nextTime
# diff = 2 nextTime + 1
# diff = 3 nextTime
# if currentTime > nextTime take currentTime + 1

s = Solution()
print(s.minimumTime([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]))
print(s.minimumTime([[0, 2, 4], [3, 2, 1], [1, 0, 4]]))

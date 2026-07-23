import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = {(0, 0)}
        q = [(0, 0, 0, 2)]  # (timeTaken, x, y, cost)

        while q:
            timeTaken, x, y, cost = heapq.heappop(q)

            if x == m - 1 and y == n - 1:
                return timeTaken

            for i in range(4):
                newX = x + directions[i][0]
                newY = y + directions[i][1]

                newCost = 1 if cost == 2 else 2
                if newX < 0 or newY < 0 or newX == m or newY == n or (newX, newY) in visited:
                    continue
                newTime = newCost + max(timeTaken, moveTime[newX][newY])
                heapq.heappush(q, (newTime, newX, newY, newCost))
                visited.add((newX, newY))


solution = Solution()
print(solution.minTimeToReach([[0, 4], [4, 4]]))
print(solution.minTimeToReach([[0, 0, 0, 0], [0, 0, 0, 0]]))
print(solution.minTimeToReach([[0, 1], [1, 2]]))

from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        result = [[-1 for i in range(n)] for i in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    q.append((i, j))
                    result[i][j] = 0

        while q:
            x, y = q.popleft()

            for i in range(4):
                newX = x + directions[i][0]
                newY = y + directions[i][1]

                if newX < 0 or newY < 0 or newX == m or newY == n or result[newX][newY] != -1:
                    continue
                result[newX][newY] = result[x][y] + 1
                q.append((newX, newY))
        return result


s = Solution()
print(s.highestPeak([[0, 1], [0, 0]]))
print(s.highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))

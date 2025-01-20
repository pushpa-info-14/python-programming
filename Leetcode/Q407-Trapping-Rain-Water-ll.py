import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        if m < 3 or n < 3: return 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = []
        waterLevel = 0
        trappedVolume = 0

        for i in range(m):
            for j in range(n):
                if i in [0, m - 1] or j in [0, n - 1]:
                    heapq.heappush(q, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        while q:
            height, x, y = heapq.heappop(q)
            waterLevel = max(waterLevel, height)
            trappedVolume += waterLevel - height

            for i in range(4):
                newX = x + directions[i][0]
                newY = y + directions[i][1]

                if newX < 0 or newY < 0 or newX == m or newY == n or heightMap[newX][newY] == -1:
                    continue

                heapq.heappush(q, (heightMap[newX][newY], newX, newY))
                heightMap[newX][newY] = -1
        return trappedVolume


s = Solution()
print(s.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
print(s.trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))

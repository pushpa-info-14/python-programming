import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        if m < 3 or n < 3: return 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        q = []
        waterLevel = 0
        trappedVolume = 0

        for i in range(m):
            heapq.heappush(q, (heightMap[i][0], i, 0))
            heapq.heappush(q, (heightMap[i][n - 1], i, n - 1))
            visited.add((i, 0))
            visited.add((i, n - 1))
        for j in range(1, n - 1):
            heapq.heappush(q, (heightMap[0][j], 0, j))
            heapq.heappush(q, (heightMap[m - 1][j], m - 1, j))
            visited.add((0, j))
            visited.add((m - 1, j))
        while q:
            height, x, y = heapq.heappop(q)
            waterLevel = max(waterLevel, height)
            if height < waterLevel:
                trappedVolume += waterLevel - height

            for i in range(4):
                newX = x + directions[i][0]
                newY = y + directions[i][1]

                if newX < 0 or newY < 0 or newX == m or newY == n or (newX, newY) in visited:
                    continue

                heapq.heappush(q, (heightMap[newX][newY], newX, newY))
                visited.add((newX, newY))
        return trappedVolume


s = Solution()
print(s.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))

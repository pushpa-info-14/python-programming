import heapq
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        heaps = []
        for r in range(m):
            heaps.append(grid[r])
            heapq.heapify(heaps[r])
        res = 0
        for c in range(n):
            x = 0
            for r in range(m):
                x = max(x, heaps[r][0])
                heapq.heappop(heaps[r])
            res += x
        return res


s = Solution()
print(s.deleteGreatestValue(grid=[[1, 2, 4], [3, 3, 1]]))
print(s.deleteGreatestValue(grid=[[10]]))

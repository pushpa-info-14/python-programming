import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for i in range(len(points)):
            square = pow(points[i][0], 2) + pow(points[i][1], 2)
            heapq.heappush(q, (square, i))

        res = []
        for i in range(k):
            _, index = heapq.heappop(q)
            res.append(points[index])

        return res


s = Solution()
print(s.kClosest([[1, 3], [-2, 2]], 1))
print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))

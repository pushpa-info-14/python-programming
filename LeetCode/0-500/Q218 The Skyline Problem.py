import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for building in buildings:
            start,end,height = building
            points.append((start, -height))
            points.append((end, height))
        points.sort()
        res = []
        q = [0]
        prev = 0

        for point in points:
            x, height = point
            if height < 0:
                heapq.heappush(q, height)
            else:
                q.remove(-height)
                heapq.heapify(q)
            cur = q[0]
            if cur != prev:
                res.append([x, abs(cur)])
                prev = cur

        return res


# Better solution will be using Segment Tree
s = Solution()
print(s.getSkyline(buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(s.getSkyline(buildings=[[0, 2, 3], [2, 5, 3]]))
print(s.getSkyline(buildings=[[0, 2147483647, 2147483647]]))

from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        for i in range(1, n):
            dx = abs(points[i][0] - points[i - 1][0])
            dy = abs(points[i][1] - points[i - 1][1])
            res += max(dx, dy)
        return res


s = Solution()
print(s.minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]]))
print(s.minTimeToVisitAllPoints(points=[[3, 2], [-2, 2]]))

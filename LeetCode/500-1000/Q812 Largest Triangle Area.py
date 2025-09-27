from typing import List


def triangle_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        points.sort()
        points = sorted(points, key=lambda x: x[1], reverse=True)
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    res = max(res, triangle_area(points[i], points[j], points[k]))
        return res


s = Solution()
print(s.largestTriangleArea(points=[[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
print(s.largestTriangleArea(points=[[1, 0], [0, 0], [0, 1]]))
print(s.largestTriangleArea(points=[[8,10],[2,7],[9,2],[4,10]]))

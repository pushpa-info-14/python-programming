from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        inf = 10 ** 9
        x1, x2, x3 = points[0][0], points[1][0], points[2][0]
        y1, y2, y3 = points[0][1], points[1][1], points[2][1]
        if x2 - x1 == 0:
            if y2 == y1:
                return False
            m1 = inf
        else:
            m1 = (y2 - y1) / (x2 - x1)
        if x3 - x2 == 0:
            if y3 == y2:
                return False
            m2 = inf
        else:
            m2 = (y3 - y2) / (x3 - x2)
        return m1 != m2


s = Solution()
print(s.isBoomerang(points=[[1, 1], [2, 3], [3, 2]]))
print(s.isBoomerang(points=[[1, 1], [2, 2], [3, 3]]))
print(s.isBoomerang(points=[[0, 0], [1, 1], [1, 1]]))

from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coordinates = [i[0] for i in points]
        x_coordinates.sort()
        res = 0
        for i in range(1, len(x_coordinates)):
            res = max(res, x_coordinates[i] - x_coordinates[i - 1])
        return res


s = Solution()
print(s.maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]))
print(s.maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))

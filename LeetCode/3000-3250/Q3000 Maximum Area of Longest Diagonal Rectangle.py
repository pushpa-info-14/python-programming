from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_d = -1
        max_area = -1
        for length, width in dimensions:
            d = length * length + width * width
            area = length * width
            if d > max_d or (d == max_d and area > max_area):
                max_d = d
                max_area = length * width
        return max_area


s = Solution()
print(s.areaOfMaxDiagonal(dimensions=[[9, 3], [8, 6]]))
print(s.areaOfMaxDiagonal(dimensions=[[3, 4], [4, 3]]))

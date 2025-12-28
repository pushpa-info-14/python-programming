import bisect
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        l, r = 0, len(grid[0])
        for i in range(len(grid)):
            l = 0
            while l < r:
                mid = (l + r) // 2
                if grid[i][mid] < 0:
                    r = mid
                else:
                    l = mid + 1
            result += (len(grid[0]) - r)

        return result

    def countNegatives2(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        result = 0
        for i in range(len(grid)):
            result += n - bisect.bisect_right(grid[i], 0, key=lambda x: -x)
        return result


s = Solution()
print(s.countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(s.countNegatives(grid=[[3, 2], [1, 0]]))
print("---------------")
print(s.countNegatives2(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(s.countNegatives2(grid=[[3, 2], [1, 0]]))

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


s = Solution()
print(s.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(s.countNegatives([[3, 2], [1, 0]]))

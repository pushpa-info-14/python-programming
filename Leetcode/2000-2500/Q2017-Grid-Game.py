import math
from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if n < 2:
            return 0

        top_sum = 0
        min_sum = math.inf
        bottom_sum = 0

        for i in grid[0]:
            top_sum += i

        for i in range(n):
            top_sum -= grid[0][i]
            if i > 0:
                bottom_sum += grid[1][i - 1]
            second_robot = max(top_sum, bottom_sum)
            min_sum = min(min_sum, second_robot)
        return min_sum


s = Solution()
print(s.gridGame([[2, 5, 4], [1, 5, 1]]))
print(s.gridGame([[3,3,1],[8,5,2]]))

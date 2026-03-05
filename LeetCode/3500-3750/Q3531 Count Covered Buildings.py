import math
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_min = [math.inf] * (n + 1)
        x_max = [-math.inf] * (n + 1)
        y_min = [math.inf] * (n + 1)
        y_max = [-math.inf] * (n + 1)
        for x, y in buildings:
            x_min[y] = min(x_min[y], x)
            x_max[y] = max(x_max[y], x)
            y_min[x] = min(y_min[x], y)
            y_max[x] = max(y_max[x], y)
        res = 0
        for x, y in buildings:
            if x_min[y] < x < x_max[y] and y_min[x] < y < y_max[x]:
                res += 1
        return res


s = Solution()
print(s.countCoveredBuildings(n=3, buildings=[[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]))
print(s.countCoveredBuildings(n=3, buildings=[[1, 1], [1, 2], [2, 1], [2, 2]]))
print(s.countCoveredBuildings(n=5, buildings=[[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]))

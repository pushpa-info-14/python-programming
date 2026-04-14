from functools import cache
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort(key=lambda x: x[0])
        robot.sort()

        @cache
        def dp(index1, index2):
            if index1 >= len(robot):
                return 0
            if index2 >= len(factory):
                return float("inf")

            pos, lim = factory[index2]
            res = float("inf")
            current = 0

            res = min(res, dp(index1, index2 + 1))

            for i in range(index1, min(index1 + lim, len(robot))):
                current += abs(pos - robot[i])
                res = min(res, current + dp(i + 1, index2 + 1))

            return res

        return dp(0, 0)


s = Solution()
print(s.minimumTotalDistance(robot=[0, 4, 6], factory=[[2, 2], [6, 2]]))
print(s.minimumTotalDistance(robot=[1, -1], factory=[[-2, 1], [2, 1]]))

import math
from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = math.inf
        for start, t in tasks:
            res = min(res, start + t)
        return res


s = Solution()
print(s.earliestTime(tasks=[[1, 6], [2, 3]]))
print(s.earliestTime(tasks=[[100, 100], [100, 100], [100, 100]]))

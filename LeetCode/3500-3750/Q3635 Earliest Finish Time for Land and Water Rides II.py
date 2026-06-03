import math
from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                           waterDuration: List[int]) -> int:
        def solve(s1, d1, s2, d2):
            f1 = math.inf
            for i in range(len(s1)):
                f1 = min(f1, s1[i] + d1[i])
            f2 = math.inf
            for i in range(len(s2)):
                f2 = min(f2, max(f1, s2[i]) + d2[i])
            return f2

        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration)
        )


s = Solution()
print(s.earliestFinishTime(landStartTime=[2, 8], landDuration=[4, 1], waterStartTime=[6], waterDuration=[3]))
print(s.earliestFinishTime(landStartTime=[5], landDuration=[3], waterStartTime=[1], waterDuration=[10]))

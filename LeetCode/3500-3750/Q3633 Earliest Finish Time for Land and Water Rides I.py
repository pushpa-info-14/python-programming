import math
from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                           waterDuration: List[int]) -> int:
        res = math.inf
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land = landStartTime[i] + landDuration[i]
                land_water = max(land, waterStartTime[j]) + waterDuration[j]
                res = min(res, land_water)

                water = waterStartTime[j] + waterDuration[j]
                water_land = max(water, landStartTime[i]) + landDuration[i]
                res = min(res, water_land)
        return res


s = Solution()
print(s.earliestFinishTime(landStartTime=[2, 8], landDuration=[4, 1], waterStartTime=[6], waterDuration=[3]))
print(s.earliestFinishTime(landStartTime=[5], landDuration=[3], waterStartTime=[1], waterDuration=[10]))

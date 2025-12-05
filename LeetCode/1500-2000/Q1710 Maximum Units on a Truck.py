from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        cur = 0
        boxTypes.sort(key=lambda x: -x[1])
        for boxes, units in boxTypes:
            if cur + boxes <= truckSize:
                res += boxes * units
                cur += boxes
            else:
                res += (truckSize - cur) * units
                break
        return res


s = Solution()
print(s.maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4))
print(s.maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10))

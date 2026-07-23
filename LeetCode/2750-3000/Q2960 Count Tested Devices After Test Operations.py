from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        res = 0
        decrease = 0
        for i in range(n):
            if max(0, batteryPercentages[i] - decrease) > 0:
                res += 1
                decrease += 1
        return res


s = Solution()
print(s.countTestedDevices(batteryPercentages=[1, 1, 2, 1, 3]))
print(s.countTestedDevices(batteryPercentages=[0, 1, 2]))

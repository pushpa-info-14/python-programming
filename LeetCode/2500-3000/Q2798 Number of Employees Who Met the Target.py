from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for x in hours:
            if x >= target:
                res += 1
        return res


s = Solution()
print(s.numberOfEmployeesWhoMetTarget(hours=[0, 1, 2, 3, 4], target=2))
print(s.numberOfEmployeesWhoMetTarget(hours=[5, 1, 4, 2, 2], target=6))

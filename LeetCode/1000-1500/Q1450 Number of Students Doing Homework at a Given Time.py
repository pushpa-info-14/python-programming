from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n = len(startTime)
        res = 0
        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1
        return res


s = Solution()
print(s.busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4))
print(s.busyStudent(startTime=[4], endTime=[4], queryTime=4))

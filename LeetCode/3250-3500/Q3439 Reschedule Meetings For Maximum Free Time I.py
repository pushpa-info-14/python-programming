from itertools import accumulate
from operator import sub
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        startTime = startTime + [eventTime]
        endTime = [0] + endTime
        n = len(startTime)
        res = 0
        cur_sum = 0
        l = 0
        for r in range(n):
            cur_sum += (startTime[r] - endTime[r])
            if r - l + 1 > k + 1:
                cur_sum -= (startTime[l] - endTime[l])
                l += 1
            res = max(res, cur_sum)
        return res

    def maxFreeTime2(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        ps = [0] + list(accumulate(map(sub, startTime + [eventTime], [0] + endTime)))
        return max(ps[i + 1] - ps[i - k] for i in range(k, len(ps) - 1))


s = Solution()
print(s.maxFreeTime(eventTime=5, k=1, startTime=[1, 3], endTime=[2, 5]))
print(s.maxFreeTime(eventTime=10, k=1, startTime=[0, 2, 9], endTime=[1, 4, 10]))
print(s.maxFreeTime(eventTime=5, k=2, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]))
print(s.maxFreeTime2(eventTime=5, k=1, startTime=[1, 3], endTime=[2, 5]))
print(s.maxFreeTime2(eventTime=10, k=1, startTime=[0, 2, 9], endTime=[1, 4, 10]))
print(s.maxFreeTime2(eventTime=5, k=2, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]))

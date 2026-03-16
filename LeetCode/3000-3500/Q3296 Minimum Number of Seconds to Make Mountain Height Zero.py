import heapq
import math
from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        q = []
        for x in workerTimes:
            heapq.heappush(q, (x, x, x + x))
        res = 0
        while mountainHeight:
            acc, cost, next_cost = heapq.heappop(q)
            res = acc
            heapq.heappush(q, (acc + next_cost, cost, next_cost + cost))
            mountainHeight -= 1
        return res

    def minNumberOfSeconds2(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_reduce(target):
            count = 0
            for t in workerTimes:
                count += int(math.sqrt(mid / t * 2 + 0.25) - 0.5)
                if count >= mountainHeight:
                    return True
            return False

        low, high = 0, max(workerTimes) * (1 + mountainHeight) * mountainHeight // 2
        while low <= high:
            mid = (low + high) // 2
            if can_reduce(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low


s = Solution()
print(s.minNumberOfSeconds(mountainHeight=4, workerTimes=[2, 1, 1]))
print(s.minNumberOfSeconds(mountainHeight=10, workerTimes=[3, 2, 2, 4]))
print(s.minNumberOfSeconds(mountainHeight=5, workerTimes=[1]))
print("----------")
print(s.minNumberOfSeconds2(mountainHeight=4, workerTimes=[2, 1, 1]))
print(s.minNumberOfSeconds2(mountainHeight=10, workerTimes=[3, 2, 2, 4]))
print(s.minNumberOfSeconds2(mountainHeight=5, workerTimes=[1]))
print(s.minNumberOfSeconds2(mountainHeight=100000, workerTimes=[1000000]))

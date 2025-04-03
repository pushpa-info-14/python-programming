import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def total_hours(rate):
            total = 0
            for pile in piles:
                total += int(math.ceil(pile / rate))
            return total

        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2

            hours = total_hours(mid)
            if hours <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low


s = Solution()
print(s.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(s.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(s.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))

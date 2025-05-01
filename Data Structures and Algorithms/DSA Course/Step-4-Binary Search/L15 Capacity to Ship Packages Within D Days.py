from typing import List


def numOfDays(weights, capacity):
    days = 0
    count = 0
    for w in weights:
        count += w
        if count > capacity:
            days += 1
            count = w
    if count:
        days += 1
    return days


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)

        max_weight = max(weights)
        low, high = max_weight, max_weight * n
        while low <= high:
            mid = (low + high) // 2

            if numOfDays(weights, mid) <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low


s = Solution()
print(s.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
print(s.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
print(s.shipWithinDays(weights=[1, 2, 3, 1, 1], days=4))
print(s.shipWithinDays(weights=[5,5,5,5,5,5,5,5,5,5], days=8))

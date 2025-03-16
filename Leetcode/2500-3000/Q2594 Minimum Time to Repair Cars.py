from math import sqrt
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def count_repaired(time):
            count = 0
            for rank in ranks:
                count += int(sqrt(time / rank))
            return count

        res = -1
        l, r = 1, ranks[0] * cars * cars
        while l <= r:
            m = (l + r) // 2
            repaired = count_repaired(m)
            if repaired >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res


s = Solution()
print(s.repairCars(ranks=[4, 2, 3, 1], cars=10))
print(s.repairCars(ranks=[5, 1, 8], cars=6))

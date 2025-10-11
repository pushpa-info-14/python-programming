from math import inf
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        res = -inf
        energy.reverse()
        for start in range(k):
            total = 0
            for i in range(start, n, k):
                total += energy[i]
                res = max(res, total)
        return res

    # This gives a TLE
    def maximumEnergy2(self, energy: List[int], k: int) -> int:
        n = len(energy)
        res = -inf
        for i in range(n):
            total = 0
            for j in range(i, n, k):
                total += energy[j]
            res = max(res, total)
        return res


s = Solution()
print(s.maximumEnergy(energy=[5, 2, -10, -5, 1], k=3))
print(s.maximumEnergy(energy=[-2, -3, -1], k=2))
print(s.maximumEnergy2(energy=[5, 2, -10, -5, 1], k=3))
print(s.maximumEnergy2(energy=[-2, -3, -1], k=2))

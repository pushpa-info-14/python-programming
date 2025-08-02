import math
from collections import defaultdict
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)
        freq = defaultdict(int)
        min_value = math.inf
        for i in range(n):
            freq[basket1[i]] += 1
            freq[basket2[i]] -= 1
            min_value = min(min_value, basket1[i], basket2[i])

        for f in freq.values():
            if abs(f) % 2:
                return -1

        transfer = []
        for num in freq.keys():
            diff = abs(freq[num])
            if diff > 0:
                for i in range(diff // 2):
                    transfer.append(num)
        transfer.sort()

        res = 0
        for num in transfer[:len(transfer) // 2]:
            res += min(num, 2 * min_value)

        return res


s = Solution()
print(s.minCost(basket1=[4, 2, 2, 2], basket2=[1, 4, 1, 2]))
print(s.minCost(basket1=[2, 3, 4, 1], basket2=[3, 2, 5, 1]))
print(s.minCost(basket1=[84, 80, 43, 8, 80, 88, 43, 14, 100, 88], basket2=[32, 32, 42, 68, 68, 100, 42, 84, 14, 8]))

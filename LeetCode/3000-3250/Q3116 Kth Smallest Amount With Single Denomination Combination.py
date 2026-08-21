from bisect import bisect_left
from itertools import combinations
from math import lcm
from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def score(x):
            res = 0

            for i in range(1, len(coins) + 1):
                sign = 1 if i % 2 == 1 else -1
                for subset in combinations(coins, i):
                    res += sign * (x // lcm(*subset))

            return res

        return bisect_left(range(min(coins) * k + 1), k, key=score)

    def findKthSmallest2(self, coins: List[int], k: int) -> int:

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        def lcm(a, b):
            if a == 0 or b == 0:
                return 0
            return abs(a * b) // gcd(a, b)

        coins.sort()
        n = len(coins)
        m = 1 << n
        bit_counts = [0] * m
        lcms = [0] * m

        for mask in range(1, m):
            cur_lcm = 1
            for i, coin in enumerate(coins):
                if mask >> i & 1:
                    cur_lcm = lcm(cur_lcm, coin)
                    bit_counts[mask] += 1
            lcms[mask] = cur_lcm

        def count(x):
            res = 0
            for mask in range(1, m):
                if lcms[mask] > x:
                    continue
                if bit_counts[mask] & 1:
                    res += x // lcms[mask]
                else:
                    res -= x // lcms[mask]
            return res

        low, high = k, coins[0] * k + 1
        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


s = Solution()
print(s.findKthSmallest(coins=[3, 6, 9], k=3))
print(s.findKthSmallest(coins=[5, 2], k=7))
print("-----------")
print(s.findKthSmallest2(coins=[3, 6, 9], k=3))
print(s.findKthSmallest2(coins=[5, 2], k=7))

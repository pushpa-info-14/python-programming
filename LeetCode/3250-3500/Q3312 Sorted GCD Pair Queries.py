from bisect import bisect_left
from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        1. Get frequencies
        2. count[i] = Number of elements divisible by i
        3. count[i] = Pairs with both numbers divisible by i
        4. count[i] = Pairs with GCD of i
        5. count[i] = Pairs with GCD of i or less
        6. Answer queries with binary search
        """
        maxi = max(nums)
        count = [0] * (maxi + 1)
        for num in nums:
            count[num] += 1
        for i in range(1, maxi + 1):
            for j in range(i * 2, maxi + 1, i):
                count[i] += count[j]
        for i in range(1, maxi + 1):
            count[i] = count[i] * (count[i] - 1) // 2
        for i in range(maxi, 0, -1):
            for j in range(i * 2, maxi + 1, i):
                count[i] -= count[j]
        for i in range(1, maxi + 1):
            count[i] += count[i - 1]
        res = []
        for q in queries:
            q += 1
            pos = bisect_left(count, q)
            res.append(pos)
        return res


s = Solution()
print(s.gcdValues(nums=[2, 3, 4], queries=[0, 2, 2]))
print(s.gcdValues(nums=[4, 4, 2, 1], queries=[5, 3, 1, 0]))
print(s.gcdValues(nums=[2, 2], queries=[0, 0]))

import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums

        n = len(nums)
        count = [0] * n
        mod = 10 ** 9 + 7
        q = [[num, idx] for idx, num in enumerate(nums)]
        heapq.heapify(q)

        while k and q[0][0] < 1e9:
            k -= 1
            num, idx = heapq.heappop(q)
            count[idx] += 1
            heapq.heappush(q, [num * multiplier, idx])

        quotient = k // n
        remainder = k % n
        q.sort()
        for i, (num, idx) in enumerate(q):
            count[idx] += quotient + (i < remainder)

        for i in range(n):
            nums[i] *= pow(multiplier, count[i], mod)
            nums[i] %= mod

        return nums


s = Solution()
print(s.getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))
print(s.getFinalState(nums=[100000, 2000], k=2, multiplier=1000000))
print(s.getFinalState(nums=[1], k=3, multiplier=10))
print(s.getFinalState(nums=[2, 1], k=3, multiplier=10))  # [20,100]
print(s.getFinalState(nums=[66307295, 441787703, 589039035, 322281864], k=900900704,
                      multiplier=641725))  # [664480092,763599523,886046925,47878852]

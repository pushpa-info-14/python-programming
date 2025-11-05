import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        q = []
        for i in range(n):
            heapq.heappush(q, (nums[i], i))
        for i in range(k):
            num, index = heapq.heappop(q)
            num *= multiplier
            heapq.heappush(q, (num, index))
        res = [0] * n
        while q:
            num, index = heapq.heappop(q)
            res[index] = num
        return res


s = Solution()
print(s.getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))
print(s.getFinalState(nums=[1, 2], k=3, multiplier=4))

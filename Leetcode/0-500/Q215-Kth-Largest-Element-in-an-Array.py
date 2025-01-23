import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []

        for num in nums:
            heapq.heappush(q, -num)
        res = 0
        for i in range(k):
            res = -(heapq.heappop(q))
        return res


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

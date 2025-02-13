import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            z = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, z)
            operations += 1
        return operations


s = Solution()
print(s.minOperations([2, 11, 10, 1, 3], 10))
print(s.minOperations([1, 1, 2, 4, 9], 20))

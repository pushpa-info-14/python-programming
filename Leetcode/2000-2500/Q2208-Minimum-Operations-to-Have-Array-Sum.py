import heapq
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += -nums[i]
            nums[i] = -nums[i]
        heapq.heapify(nums)
        half = total / 2
        operations = 0
        while nums:
            if total < half:
                x = heapq.heappop(nums)
                y = x / 2
                total -= y
                heapq.heappush(nums, y)
                operations += 1
            else:
                return operations


s = Solution()
print(s.halveArray([5, 19, 8, 1]))
print(s.halveArray([3, 8, 20]))

import heapq
import math
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        min_heap = []
        max_heap = []
        r_max_sum = [0] * n
        l_sum = 0
        r_sum = 0
        p1 = n // 3
        p2 = 2 * n // 3

        for i in reversed(range(p1, n)):
            heapq.heappush(min_heap, nums[i])
            r_sum += nums[i]

            while len(min_heap) > p1:
                r_sum -= heapq.heappop(min_heap)

            if len(min_heap) == p1:
                r_max_sum[i] = r_sum

        res = math.inf
        for i in range(p2):
            heapq.heappush(max_heap, -nums[i])
            l_sum += nums[i]

            while len(max_heap) > p1:
                l_sum += heapq.heappop(max_heap)

            if len(max_heap) == p1:
                res = min(res, l_sum - r_max_sum[i + 1])
        return res


s = Solution()
print(s.minimumDifference(nums=[3, 1, 2]))
print(s.minimumDifference(nums=[7, 9, 5, 8, 1, 3]))
print(s.minimumDifference(nums=[2, 3, 1, 8, 5, 4]))

import math
from typing import List


class Solution:
    def maxSubarraySumTLE(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = nums[i] + prefix_sum[i]

        res = -math.inf
        for i in range(n):
            for j in range(i + k - 1, n, k):
                res = max(res, prefix_sum[j + 1] - prefix_sum[i])
        return res

    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [math.inf] * k
        prefix[0] = 0
        res = -math.inf
        total = 0
        for i in range(n):
            total += nums[i]
            rem = (i + 1) % k
            res = max(res, total - prefix[rem])
            prefix[rem] = min(prefix[rem], total)
        return res


s = Solution()
print(s.maxSubarraySumTLE(nums=[1, 2], k=1))
print(s.maxSubarraySumTLE(nums=[-1, -2, -3, -4, -5], k=4))
print(s.maxSubarraySumTLE(nums=[-5, 1, 2, -3, 4], k=2))
print(s.maxSubarraySum(nums=[1, 2], k=1))
print(s.maxSubarraySum(nums=[-1, -2, -3, -4, -5], k=4))
print(s.maxSubarraySum(nums=[-5, 1, 2, -3, 4], k=2))

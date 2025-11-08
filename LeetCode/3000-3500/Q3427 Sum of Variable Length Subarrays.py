from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        for i in range(n):
            start = max(0, i - nums[i])
            res += prefix_sum[i + 1] - prefix_sum[start]
        return res


s = Solution()
print(s.subarraySum(nums=[2, 3, 1]))
print(s.subarraySum(nums=[3, 1, 1, 2]))

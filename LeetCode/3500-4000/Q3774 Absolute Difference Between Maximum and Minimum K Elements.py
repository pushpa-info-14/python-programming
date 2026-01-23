from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = nums[i] + pre_sum[i]
        min_sum = pre_sum[k]
        max_sum = pre_sum[n] - pre_sum[n - k]
        return max_sum - min_sum


s = Solution()
print(s.absDifference(nums=[5, 2, 2, 4], k=2))
print(s.absDifference(nums=[100], k=1))

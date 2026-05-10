from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for i in range(n):
            if dp[i] >= 0:
                for j in range(i + 1, n):
                    if -target <= nums[j] - nums[i] <= target:
                        dp[j] = max(dp[j], dp[i] + 1)
        return dp[-1]


s = Solution()
print(s.maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=2))
print(s.maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=3))
print(s.maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=0))
print(s.maximumJumps(nums=[1, 0, 2], target=1))
print(s.maximumJumps(nums=[1, 0, 3, 4, 2], target=2))

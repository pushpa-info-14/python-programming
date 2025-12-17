from typing import List


class Solution:
    def lis(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):  # Starts from 1 and look back
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        print(dp)
        return dp[n - 1]


s = Solution()
print(s.lis([3, 1, 8, 2, 5]))

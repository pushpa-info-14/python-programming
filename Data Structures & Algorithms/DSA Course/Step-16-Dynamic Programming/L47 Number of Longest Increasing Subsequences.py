from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        counts = [1] * n
        maxi = 1

        for i in range(n):
            for prev in range(i):
                if nums[prev] < nums[i]:
                    if dp[i] < 1 + dp[prev]:
                        dp[i] = 1 + dp[prev]
                        counts[i] = counts[prev]
                    elif dp[i] == 1 + dp[prev]:
                        counts[i] += counts[prev]
            maxi = max(maxi, dp[i])
        res = 0
        for i in range(n):
            if dp[i] == maxi:
                res += counts[i]
        return res


# LeetCode 673
s = Solution()
print(s.findNumberOfLIS(nums=[1, 3, 5, 4, 7]))
print(s.findNumberOfLIS(nums=[2, 2, 2, 2, 2]))

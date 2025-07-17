from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            i = num % k
            for j in range(k):
                dp[i][j] = max(dp[i][j], dp[j][i] + 1)
                res = max(res, dp[i][j])
        return res


s = Solution()
print(s.maximumLength(nums=[1, 2, 3, 4, 5], k=2))
print(s.maximumLength(nums=[1, 4, 2, 3, 1, 4], k=3))

from collections import Counter
from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        dp = Counter()
        for x in sorted(nums):
            dp[x], dp[x + 1] = dp[x - 1] + 1, dp[x] + 1
        return max(dp.values())


s = Solution()
print(s.maxSelectedElements(nums=[2, 1, 5, 1, 1]))
print(s.maxSelectedElements(nums=[1, 4, 7, 10]))

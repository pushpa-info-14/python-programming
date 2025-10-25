from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        res = 0
        for num in nums:
            res += dp[num]
            dp[num] += 1
        return res


s = Solution()
print(s.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
print(s.numIdenticalPairs(nums=[1, 1, 1, 1]))
print(s.numIdenticalPairs(nums=[1, 2, 3]))

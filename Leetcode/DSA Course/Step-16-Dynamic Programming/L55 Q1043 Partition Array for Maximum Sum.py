import math
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def dfs(index):
            if index == n: return 0
            if dp[index] != -1: return dp[index]

            length = 0
            max_val = -math.inf
            res = -math.inf
            for i in range(index, min(index + k, n)):
                length += 1
                max_val = max(max_val, arr[i])
                cur_sum = length * max_val + dfs(i + 1)
                res = max(res, cur_sum)
            dp[index] = res
            return res

        return dfs(0)


s = Solution()
print(s.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
print(s.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
print(s.maxSumAfterPartitioning([1], 1))

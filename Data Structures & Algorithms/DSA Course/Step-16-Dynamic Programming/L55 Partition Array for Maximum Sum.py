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


    def maxSumAfterPartitioningTabulation(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        dp[n] = 0

        for index in range(n-1, -1, -1):
            length = 0
            max_val = -math.inf
            res = -math.inf
            for i in range(index, min(index + k, n)):
                length += 1
                max_val = max(max_val, arr[i])
                cur_sum = length * max_val + dp[i + 1]
                res = max(res, cur_sum)
            dp[index] = res

        return dp[0]


# LeetCode 1043
s = Solution()
print(s.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
print(s.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
print(s.maxSumAfterPartitioning([1], 1))
print("-----------------------------------------")
print(s.maxSumAfterPartitioningTabulation([1, 15, 7, 9, 2, 5, 10], 3))
print(s.maxSumAfterPartitioningTabulation([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
print(s.maxSumAfterPartitioningTabulation([1], 1))

from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2

        @cache
        def dfs(i, cur):
            if cur == 0:
                return True
            if i == 0:
                return nums[i] == cur
            not_take = dfs(i - 1, cur)
            take = False
            if nums[i] <= target:
                take = dfs(i - 1, cur - nums[i])
            return not_take or take

        return dfs(n - 1, target)

    def canPartition2(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for cur in range(1, target + 1):
                not_take = dp[i - 1][cur]
                take = False
                if nums[i] <= target:
                    take = dp[i - 1][cur - nums[i]]
                dp[i][cur] = not_take or take
        return dp[n - 1][target]


# LeetCode 416
s = Solution()
print(s.canPartition(nums=[1, 5, 11, 5]))
print(s.canPartition(nums=[1, 2, 3, 5]))
print(s.canPartition2(
    nums=[71, 70, 66, 54, 32, 63, 38, 98, 4, 22, 61, 40, 6, 8, 6, 21, 71, 36, 30, 34, 44, 60, 89, 53, 60, 56, 73, 14,
          63, 37, 15, 58, 51, 88, 88, 32, 80, 32, 10, 89, 67, 29, 68, 65, 34, 15, 88, 8, 57, 78, 37, 63, 73, 65, 47, 39,
          32, 74, 31, 44, 43, 4, 10, 8, 96, 22, 58, 87, 29, 99, 79, 13, 96, 21, 62, 71, 34, 55, 72, 3, 96, 7, 36, 64,
          30, 6, 14, 87, 12, 90, 40, 13, 29, 21, 94, 33, 99, 86, 4, 100]))

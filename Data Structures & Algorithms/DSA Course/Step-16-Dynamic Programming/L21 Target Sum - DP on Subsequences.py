from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        if (total - target) < 0 or (total - target) & 1:
            return 0
        k = (total - target) // 2
        memo = {}

        def dfs(i, cur):
            if (i, cur) in memo:
                return memo[(i, cur)]
            if i == 0:
                if cur == 0 and nums[0] == 0:
                    return 2
                if cur == 0 or cur == nums[0]:
                    return 1
                return 0
            not_take = dfs(i - 1, cur)
            take = 0
            if nums[i] <= cur:
                take = dfs(i - 1, cur - nums[i])
            memo[(i, cur)] = not_take + take
            return memo[(i, cur)]

        return dfs(n - 1, k)

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        if (total - target) < 0 or (total - target) & 1:
            return 0
        k = (total - target) // 2
        dp = [[0] * (k + 1) for _ in range(n)]

        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        if nums[0] != 0 and nums[0] <= k:
            dp[0][nums[0]] = 1

        for i in range(1, n):
            for cur in range(k + 1):
                not_take = dp[i - 1][cur]
                take = 0
                if nums[i] <= cur:
                    take = dp[i - 1][cur - nums[i]]
                dp[i][cur] = not_take + take

        return dp[n - 1][k]


s = Solution()
print(s.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))  # 5
print(s.findTargetSumWays(nums=[1], target=1))  # 1
print(s.findTargetSumWays(nums=[0], target=0))  # 2
print(s.findTargetSumWays(nums=[0, 0, 0, 0, 0, 0, 0, 0, 1], target=1))  # 256
print("-------------------------")
print(s.findTargetSumWays2(nums=[1, 1, 1, 1, 1], target=3))  # 5
print(s.findTargetSumWays2(nums=[1], target=1))  # 1
print(s.findTargetSumWays2(nums=[0], target=0))  # 2
print(s.findTargetSumWays2(nums=[0, 0, 0, 0, 0, 0, 0, 0, 1], target=1))  # 256

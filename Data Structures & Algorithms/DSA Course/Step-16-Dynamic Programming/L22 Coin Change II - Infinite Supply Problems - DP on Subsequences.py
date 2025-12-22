from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}

        def dfs(i, target):
            if (i, target) in memo:
                return memo[(i, target)]
            if target == 0:
                return 1
            if i == 0:
                if target % coins[i] == 0:
                    return 1
                else:
                    return 0
            not_take = dfs(i - 1, target)
            take = 0
            if coins[i] <= target:
                take = dfs(i, target - coins[i])
            memo[(i, target)] = not_take + take
            return memo[(i, target)]

        return dfs(n - 1, amount)

    def change2(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = 1

        for i in range(1, n):
            for target in range(amount + 1):
                not_take = dp[i - 1][target]
                take = 0
                if coins[i] <= target:
                    take = dp[i][target - coins[i]]
                dp[i][target] = not_take + take

        return dp[n - 1][amount]

    def change3(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        prev = [0] * (amount + 1)
        for i in range(amount + 1):
            if i % coins[0] == 0:
                prev[i] = 1

        for i in range(1, n):
            cur = [0] * (amount + 1)
            for target in range(amount + 1):
                not_take = prev[target]
                take = 0
                if coins[i] <= target:
                    take = cur[target - coins[i]]
                cur[target] = not_take + take
            prev = cur

        return prev[amount]


s = Solution()
print(s.change(amount=5, coins=[1, 2, 5]))
print(s.change(amount=3, coins=[2]))
print(s.change(amount=10, coins=[10]))
print("--------------------------")
print(s.change2(amount=5, coins=[1, 2, 5]))
print(s.change2(amount=3, coins=[2]))
print(s.change2(amount=10, coins=[10]))
print("--------------------------")
print(s.change3(amount=5, coins=[1, 2, 5]))
print(s.change3(amount=3, coins=[2]))
print(s.change3(amount=10, coins=[10]))

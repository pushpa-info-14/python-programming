from functools import cache
from typing import List


class Solution:
    def number_of_ways(self, coins: List[int], amount: int) -> int:
        coins.sort()

        @cache
        def dfs(x):
            if x == 0:
                return 1
            cur = 0
            for coin in coins:
                if coin > x:
                    break
                cur += dfs(x - coin)
            return cur

        res = dfs(amount)
        return res

    def number_of_ways2(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount + 1)
        dp[0] = 1
        for cur in range(1, amount + 1):
            for coin in coins:
                if coin > cur:
                    break
                dp[cur] += dp[cur - coin]
        return dp[amount]


s = Solution()
print(s.number_of_ways([1, 4, 5], 5))
print(s.number_of_ways([1, 4, 5], 13))
print(s.number_of_ways([1, 2, 5], 11))
print(s.number_of_ways([2], 3))
print(s.number_of_ways([1], 0))
print(s.number_of_ways([1, 2, 5], 100))
print("---------------------------------------")
print(s.number_of_ways2([1, 4, 5], 5))
print(s.number_of_ways2([1, 4, 5], 13))
print(s.number_of_ways2([1, 2, 5], 11))
print(s.number_of_ways2([2], 3))
print(s.number_of_ways2([1], 0))
print(s.number_of_ways2([1, 2, 5], 100))

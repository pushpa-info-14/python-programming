from functools import cache
from typing import List


class Solution:
    def minimum_coins(self, coins: List[int], amount: int) -> int:
        inf = 10 ** 10
        coins.sort()

        @cache
        def dfs(x):
            if x == 0:
                return 0
            cur = inf
            for coin in coins:
                if coin > x:
                    break
                cur = min(cur, 1 + dfs(x - coin))
            return cur

        res = dfs(amount)
        return res if res != inf else -1

    def minimum_coins2(self, coins: List[int], amount: int) -> int:
        inf = 10 ** 10
        coins.sort()
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for cur in range(1, amount + 1):
            for coin in coins:
                if coin > cur:
                    break
                dp[cur] = min(dp[cur], 1 + dp[cur - coin])

        res = dp[amount]
        return res if res != inf else -1


s = Solution()
print(s.minimum_coins([1, 4, 5], 13))
print(s.minimum_coins([1, 2, 5], 11))
print(s.minimum_coins([2], 3))
print(s.minimum_coins([1], 0))
print(s.minimum_coins([1, 2, 5], 100))
print("----------------------------")
print(s.minimum_coins2([1, 4, 5], 13))
print(s.minimum_coins2([1, 2, 5], 11))
print(s.minimum_coins2([2], 3))
print(s.minimum_coins2([1], 0))
print(s.minimum_coins2([1, 2, 5], 100))

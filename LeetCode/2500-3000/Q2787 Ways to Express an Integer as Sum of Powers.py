from functools import cache


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10 ** 9 + 7
        powers = []
        for num in range(1, n + 1):
            p = pow(num, x)
            if p > n:
                break
            powers.append(p)

        @cache
        def dfs(i, cur):
            if cur == n:
                return 1
            if i == len(powers) or cur > n:
                return 0
            not_include = dfs(i + 1, cur)
            include = dfs(i + 1, cur + powers[i])
            return (not_include + include) % mod

        return dfs(0, 0)

    def numberOfWays2(self, n: int, x: int) -> int:
        # 2D Tabulation
        mod = 10 ** 9 + 7
        powers = []
        for num in range(1, n + 1):
            p = pow(num, x)
            if p > n:
                break
            powers.append(p)

        dp = [[0] * (n + 1) for _ in range(len(powers) + 1)]
        for i in range(len(powers) + 1):
            dp[i][0] = 1

        for i in range(1, len(powers) + 1):
            power = powers[i - 1]
            for target in range(1, n + 1):
                if power > target:
                    dp[i][target] = dp[i - 1][target]
                else:
                    dp[i][target] = (dp[i - 1][target] + dp[i - 1][target - power]) % mod
        return dp[-1][-1]

    def numberOfWays3(self, n: int, x: int) -> int:
        # 1D Tabulation
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        # Should solve from right to left.
        for num in range(1, n + 1):
            power = pow(num, x)
            if power > n:
                break
            for target in range(n, -1, -1):
                if target >= power:
                    dp[target] = (dp[target] + dp[target - power]) % mod
        return dp[-1]


s = Solution()
print(s.numberOfWays(n=10, x=2))
print(s.numberOfWays(n=4, x=1))
print(s.numberOfWays(n=68, x=1))
print(s.numberOfWays(n=213, x=1))
print(s.numberOfWays2(n=10, x=2))
print(s.numberOfWays2(n=4, x=1))
print(s.numberOfWays2(n=68, x=1))
print(s.numberOfWays2(n=213, x=1))
print(s.numberOfWays3(n=10, x=2))
print(s.numberOfWays3(n=4, x=1))
print(s.numberOfWays3(n=68, x=1))
print(s.numberOfWays3(n=213, x=1))

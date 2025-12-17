class Solution:
    def fib1(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib1(n - 2) + self.fib1(n - 1)

    def fib2(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def fib(x):
            if x in memo:
                return memo[x]
            memo[x] = fib(x - 2) + fib(x - 1)
            return memo[x]

        return fib(n)

    def fib3(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]

    def fib4(self, n: int) -> int:
        prev0 = 0
        prev1 = 1
        for i in range(2, n + 1):
            cur = prev0 + prev1
            prev0 = prev1
            prev1 = cur
        return prev1


s = Solution()
print(s.fib1(2))
print(s.fib1(3))
print(s.fib1(4))
print(s.fib2(2))
print(s.fib2(3))
print(s.fib2(4))
print(s.fib2(100))
print(s.fib3(2))
print(s.fib3(3))
print(s.fib3(4))
print(s.fib3(100))
print(s.fib4(2))
print(s.fib4(3))
print(s.fib4(4))
print(s.fib4(100))

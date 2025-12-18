def fib1(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib1(n - 2) + fib1(n - 1)


def fib2(n, memo=None):
    if memo is None:
        memo = {}
    if n == 0: return 0
    if n == 1: return 1
    if n in memo:
        return memo[n]

    memo[n] = fib2(n - 2, memo) + fib2(n - 1, memo)
    return memo[n]


def fib3(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[n]


def fib4(n):
    prev0 = 0
    prev1 = 1
    for i in range(2, n + 1):
        cur = prev0 + prev1
        prev0 = prev1
        prev1 = cur
    return prev1


print(fib1(2))
print(fib1(10))

print(fib2(2))
print(fib2(10))
print(fib2(1000))

print(fib3(2))
print(fib3(10))
print(fib3(1000))

print(fib4(2))
print(fib4(10))
print(fib4(1000))

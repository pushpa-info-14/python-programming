def cutRod(price, n):
    memo = {}

    def dfs(i, length):
        if (i, length) in memo:
            return memo[(i, length)]
        if length == 0:
            return 0
        if i == 0:
            return length * price[i]
        not_take = dfs(i - 1, length)
        take = 0
        rod_length = i + 1
        if rod_length <= length:
            take = price[i] + dfs(i, length - rod_length)
        memo[(i, length)] = max(not_take, take)
        return memo[(i, length)]

    return dfs(n - 1, n)


def cutRod2(price, n):
    dp = [[0] * (n + 1) for _ in range(n)]
    for length in range(n + 1):
        dp[0][length] = length * price[0]

    for i in range(1, n):
        for length in range(n + 1):
            not_take = dp[i - 1][length]
            take = 0
            rod_length = i + 1
            if rod_length <= length:
                take = price[i] + dp[i][length - rod_length]
            dp[i][length] = max(not_take, take)
    return dp[n - 1][n]


def cutRod3(price, n):
    prev = [0] * (n + 1)
    for length in range(n + 1):
        prev[length] = length * price[0]

    for i in range(1, n):
        cur = [0] * (n + 1)
        for length in range(n + 1):
            not_take = prev[length]
            take = 0
            rod_length = i + 1
            if rod_length <= length:
                take = price[i] + cur[length - rod_length]
            cur[length] = max(not_take, take)
        prev = cur
    return prev[n]


def cutRod4(price, n):
    prev = [0] * (n + 1)
    for length in range(n + 1):
        prev[length] = length * price[0]

    for i in range(1, n):
        for length in range(n + 1):
            not_take = prev[length]
            take = 0
            rod_length = i + 1
            if rod_length <= length:
                take = price[i] + prev[length - rod_length]
            prev[length] = max(not_take, take)
    return prev[n]


"""
https://www.naukri.com/code360/problems/rod-cutting-problem_800284

Given a rod of length ‘N’ units. The rod can be cut into different sizes and each size has a cost 
associated with it. Determine the maximum cost obtained by cutting the rod and selling its pieces.

Note:
1. The sizes will range from 1 to ‘N’ and will be integers.

2. The sum of the pieces cut should be equal to ‘N’.

3. Consider 1-based indexing.
"""

print(cutRod([2, 5, 7, 8, 10], 5))
print(cutRod([3, 5, 8, 9, 10, 17, 17, 20], 8))
print(cutRod([3, 5, 6, 7, 10, 12], 6))
print("-------------------")
print(cutRod2([2, 5, 7, 8, 10], 5))
print(cutRod2([3, 5, 8, 9, 10, 17, 17, 20], 8))
print(cutRod2([3, 5, 6, 7, 10, 12], 6))
print("-------------------")
print(cutRod3([2, 5, 7, 8, 10], 5))
print(cutRod3([3, 5, 8, 9, 10, 17, 17, 20], 8))
print(cutRod3([3, 5, 6, 7, 10, 12], 6))
print("-------------------")
print(cutRod4([2, 5, 7, 8, 10], 5))
print(cutRod4([3, 5, 8, 9, 10, 17, 17, 20], 8))
print(cutRod4([3, 5, 6, 7, 10, 12], 6))

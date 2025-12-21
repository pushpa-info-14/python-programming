def minimumCoins(p):
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    inf = 10 ** 10
    memo = {}

    def dfs(target):
        if target in memo:
            return memo[target]
        if target == 0:
            return 0
        cur = inf
        for coin in coins:
            if coin > target:
                break
            cur = min(cur, 1 + dfs(target - coin))
        memo[target] = cur
        return memo[target]

    return dfs(p)


def minimumCoins2(p):
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    inf = 10 ** 10
    dp = [inf] * (p + 1)
    dp[0] = 0
    for target in range(1, p + 1):
        cur = inf
        for coin in coins:
            if coin > target:
                break
            cur = min(cur, 1 + dp[target - coin])
        dp[target] = cur
    return dp[p]


def minimumCoins3(p):
    original = p
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    p = p % 1000
    inf = 10 ** 10
    dp = [inf] * (p + 1)
    dp[0] = 0
    for target in range(1, p + 1):
        cur = inf
        for coin in coins:
            if coin > target:
                break
            cur = min(cur, 1 + dp[target - coin])
        dp[target] = cur
    return dp[p] + (original // 1000)


"""
https://www.naukri.com/code360/problems/minimum-coins_982764

Bob went to his favourite bakery to buy some pastries. After picking up his favourite pastries his total bill 
was P cents. Bob lives in Berland where all the money is in the form of coins with 
denominations {1, 2, 5, 10, 20, 50, 100, 500, 1000}.

Bob is not very good at maths and thinks fewer coins mean less money and he will be happy if he gives minimum 
number of coins to the shopkeeper. Help Bob to find the minimum number of coins that sums to P cents 
(assume that Bob has an infinite number of coins of all denominations).
"""

print(minimumCoins(60))
print(minimumCoins(10))
print(minimumCoins(24))
print("-------------------")
print(minimumCoins2(60))
print(minimumCoins2(10))
print(minimumCoins2(24))
print("-------------------")
print(minimumCoins3(60))
print(minimumCoins3(10))
print(minimumCoins3(24))
print(minimumCoins3(10 ** 6))

from typing import List


def unboundedKnapsack(n: int, w: int, profits: List[int], weights: List[int]) -> int:
    memo = {}

    def dfs(i, target):
        if (i, target) in memo:
            return memo[(i, target)]
        if i == 0:
            return (target // weights[0]) * profits[0]
        not_take = dfs(i - 1, target)
        take = 0
        if weights[i] <= target:
            take = profits[i] + dfs(i, target - weights[i])
        memo[(i, target)] = max(not_take, take)
        return memo[(i, target)]

    return dfs(n - 1, w)


def unboundedKnapsack2(n: int, w: int, profits: List[int], weights: List[int]) -> int:
    dp = [[0] * (w + 1) for _ in range(n)]
    for target in range(w + 1):
        dp[0][target] = (target // weights[0]) * profits[0]
    for i in range(1, n):
        for target in range(w + 1):
            not_take = dp[i - 1][target]
            take = 0
            if weights[i] <= target:
                take = profits[i] + dp[i][target - weights[i]]
            dp[i][target] = max(not_take, take)

    return dp[n - 1][w]


def unboundedKnapsack3(n: int, w: int, profits: List[int], weights: List[int]) -> int:
    prev = [0] * (w + 1)
    for target in range(w + 1):
        prev[target] = (target // weights[0]) * profits[0]
    for i in range(1, n):
        cur = [0] * (w + 1)
        for target in range(w + 1):
            not_take = prev[target]
            take = 0
            if weights[i] <= target:
                take = profits[i] + cur[target - weights[i]]
            cur[target] = max(not_take, take)
        prev = cur

    return prev[w]


def unboundedKnapsack4(n: int, w: int, profits: List[int], weights: List[int]) -> int:
    prev = [0] * (w + 1)
    for target in range(w + 1):
        prev[target] = (target // weights[0]) * profits[0]
    for i in range(1, n):
        for target in range(w + 1):
            not_take = prev[target]
            take = 0
            if weights[i] <= target:
                take = profits[i] + prev[target - weights[i]]
            prev[target] = max(not_take, take)

    return prev[w]


"""
https://www.naukri.com/code360/problems/unbounded-knapsack_1215029

You are given ‘n’ items with certain ‘profit’ and ‘weight’ and a knapsack with weight capacity ‘w’.

You need to fill the knapsack with the items in such a way that you get the maximum profit. You are allowed 
to take one item multiple times.

Example:
Input: 
'n' = 3, 'w' = 10, 
'profit' = [5, 11, 13]
'weight' = [2, 4, 6]

Output: 27

Explanation:
We can fill the knapsack as:

1 item of weight 6 and 1 item of weight 4.
1 item of weight 6 and 2 items of weight 2.
2 items of weight 4 and 1 item of weight 2.
5 items of weight 2.

The maximum profit will be from case 3 = 11 + 11 + 5 = 27. Therefore maximum profit = 27.
"""

print(unboundedKnapsack(3, 15, [7, 2, 4], [5, 10, 20]))
print(unboundedKnapsack(2, 3, [6, 12], [4, 17]))
print("------------------")
print(unboundedKnapsack2(3, 15, [7, 2, 4], [5, 10, 20]))
print(unboundedKnapsack2(2, 3, [6, 12], [4, 17]))
print("------------------")
print(unboundedKnapsack3(3, 15, [7, 2, 4], [5, 10, 20]))
print(unboundedKnapsack3(2, 3, [6, 12], [4, 17]))
print("------------------")
print(unboundedKnapsack4(3, 15, [7, 2, 4], [5, 10, 20]))
print(unboundedKnapsack4(2, 3, [6, 12], [4, 17]))

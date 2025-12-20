from typing import List


def findWays(arr: List[int], k: int) -> int:
    arr.sort(reverse=True)
    n = len(arr)
    mod = 10 ** 9 + 7
    memo = {}

    def dfs(i, cur):
        if (i, cur) in memo:
            return memo[(i, cur)]
        if cur == 0:
            return 1
        if i == 0:
            if arr[i] == cur:
                return 1
            else:
                return 0
        not_take = dfs(i - 1, cur)
        take = 0
        if arr[i] <= cur:
            take = dfs(i - 1, cur - arr[i])
        memo[(i, cur)] = take + not_take
        return memo[(i, cur)]

    return dfs(n - 1, k) % mod


def findWays2(arr: List[int], k: int) -> int:
    zeros = arr.count(0)
    n = len(arr)
    mod = 10 ** 9 + 7
    dp = [[0] * (k + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    if arr[0] <= k:
        dp[0][arr[0]] = 1
    for i in range(1, n):
        for cur in range(1, k + 1):
            not_take = dp[i - 1][cur]
            take = 0
            if arr[i] <= cur:
                take = dp[i - 1][cur - arr[i]]
            dp[i][cur] = take + not_take
    res = dp[n - 1][k]
    if zeros:
        res *= pow(2, zeros)
    return res % mod


"""
https://www.naukri.com/code360/problems/count-subsets-with-sum-k_3952532?leftPanelTabValue=PROBLEM

You are given an array 'arr' of size 'n' containing positive integers and a target sum 'k'.
Find the number of ways of selecting the elements from the array such that the sum of chosen elements is equal to the target 'k'.
Since the number of ways can be very large, print it modulo 10 ^ 9 + 7.

Example:
Input: 'arr' = [1, 1, 4, 5]

Output: 3

Explanation: The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.
"""

print(findWays([1, 4, 4, 5], 5))
print(findWays([1, 1, 1], 2))
print(findWays([2, 34, 5], 40))
print(findWays([0, 1, 3], 4))
print("------------------------------")
print(findWays2([1, 4, 4, 5], 5))
print(findWays2([1, 1, 1], 2))
print(findWays2([2, 34, 5], 40))
print(findWays2([0, 1, 3], 4))

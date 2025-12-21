class Solution:
    def knapsack(self, w, val, wt):
        n = len(val)
        memo = {}

        def dfs(i, weight):
            if (i, weight) in memo:
                return memo[(i, weight)]
            if i == 0:
                if wt[i] <= weight:
                    return val[i]
                else:
                    return 0
            not_take = dfs(i - 1, weight)
            take = 0
            if wt[i] <= weight:
                take = val[i] + dfs(i - 1, weight - wt[i])
            memo[(i, weight)] = max(not_take, take)
            return memo[(i, weight)]

        return dfs(n - 1, w)

    def knapsack2(self, w, val, wt):
        n = len(val)
        dp = [[0] * (w + 1) for _ in range(n)]
        for weight in range(wt[0], w + 1):
            dp[0][weight] = val[0]
        for i in range(1, n):
            for weight in range(1, w + 1):
                not_take = dp[i - 1][weight]
                take = 0
                if wt[i] <= weight:
                    take = val[i] + dp[i - 1][weight - wt[i]]
                dp[i][weight] = max(not_take, take)
        return dp[n - 1][w]

    def knapsack3(self, w, val, wt):
        n = len(val)
        prev = [0] * (w + 1)
        for weight in range(wt[0], w + 1):
            prev[weight] = val[0]
        for i in range(1, n):
            cur = [0] * (w + 1)
            for weight in range(1, w + 1):
                not_take = prev[weight]
                take = 0
                if wt[i] <= weight:
                    take = val[i] + prev[weight - wt[i]]
                cur[weight] = max(not_take, take)
            prev = cur
        return prev[w]


"""
https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

Given two arrays, val[] and wt[], where each element represents the value and weight of an item respectively, and an 
integer W representing the maximum capacity of the knapsack (the total weight it can hold).

The task is to put the items into the knapsack such that the total value obtained is maximum without exceeding the 
capacity W.

Note: You can either include an item completely or exclude it entirely — fractional selection of items is not allowed. 
Each item is available only once.
"""

s = Solution()
print(s.knapsack(4, [1, 2, 3], [4, 5, 1]))
print(s.knapsack(3, [1, 2, 3], [4, 5, 6]))
print(s.knapsack(5, [10, 40, 30, 50], [5, 4, 2, 3]))
print(s.knapsack(7, [10, 8, 6], [1, 7, 9]))
print("---------------------------")
print(s.knapsack2(4, [1, 2, 3], [4, 5, 1]))
print(s.knapsack2(3, [1, 2, 3], [4, 5, 6]))
print(s.knapsack2(5, [10, 40, 30, 50], [5, 4, 2, 3]))
print(s.knapsack2(7, [10, 8, 6], [1, 7, 9]))
print("---------------------------")
print(s.knapsack3(4, [1, 2, 3], [4, 5, 1]))
print(s.knapsack3(3, [1, 2, 3], [4, 5, 6]))
print(s.knapsack3(5, [10, 40, 30, 50], [5, 4, 2, 3]))
print(s.knapsack3(7, [10, 8, 6], [1, 7, 9]))

"""
# For https://www.naukri.com/code360/problems/0-1-knapsack_920542?leftPanelTabValue=SUBMISSION

t = int(input())
for i in range(t):
    n = int(input())
    wi = list(map(int, input().split()))
    vi = list(map(int, input().split()))
    w = int(input())
    print(s.knapsack(w, vi, wi))
"""


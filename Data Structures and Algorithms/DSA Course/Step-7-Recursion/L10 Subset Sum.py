# Given a list(arr) of n integers, print sum of all subsets in it.
# Output should be printed in increasing order of sums
import re


def subsetSum(arr):
    n = len(arr)
    res = []

    def dfs(i, summation):
        if i == n:
            res.append(summation)
            return
        dfs(i + 1, summation + arr[i])
        dfs(i + 1, summation)

    dfs(0, 0)
    res.sort()
    return res

print(subsetSum([2,3]))
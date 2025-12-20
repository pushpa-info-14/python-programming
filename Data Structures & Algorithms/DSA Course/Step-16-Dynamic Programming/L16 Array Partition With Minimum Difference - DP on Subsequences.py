from typing import List


def minSubsetSumDifference(arr: List[int], n: int) -> int:
    total = sum(arr)
    target = total
    dp = [[False] * (target + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    for i in range(1, n):
        for cur in range(1, target + 1):
            not_take = dp[i - 1][cur]
            take = False
            if arr[i] <= target:
                take = dp[i - 1][cur - arr[i]]
            dp[i][cur] = not_take or take
    res = total
    for sum1 in range(target + 1):
        if dp[n - 1][sum1]:
            res = min(res, abs(sum1 - (total - sum1)))
    return res


"""
https://www.naukri.com/code360/problems/array-partition-with-minimum-difference_842494

You are given an array 'arr' containing 'n' non-negative integers.
Your task is to partition this array into two subsets such that the absolute difference between subset sums is minimum.
You just need to find the minimum absolute difference considering any valid division of the array elements.

Note:
1. Each array element should belong to exactly one of the subsets.
2. Subsets need not always be contiguous.
For example, for the array : [1, 2, 3], some of the possible divisions are 
   a) {1,2} and {3}
   b) {1,3} and {2}.
3. Subset-sum is the sum of all the elements in that subset. 
"""

print(minSubsetSumDifference([3, 1, 5, 2, 8], 5))
print(minSubsetSumDifference([1, 2, 3, 4], 4))
print(minSubsetSumDifference([8, 6, 5], 3))

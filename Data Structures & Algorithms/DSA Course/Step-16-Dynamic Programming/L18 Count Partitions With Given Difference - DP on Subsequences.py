from typing import List


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    mod = 10 ** 9 + 7
    total = sum(arr)
    if (total - d) < 0 or (total - d) % 2:
        return 0
    k = (total - d) // 2
    memo = {}

    def dfs(i, cur):
        if (i, cur) in memo:
            return memo[(i, cur)]
        if i == 0:
            if cur == 0 and arr[0] == 0:
                return 2
            if cur == 0 or cur == arr[0]:
                return 1
            return 0
        not_take = dfs(i - 1, cur)
        take = 0
        if arr[i] <= cur:
            take = dfs(i - 1, cur - arr[i])
        memo[(i, cur)] = take + not_take
        return memo[(i, cur)]

    return dfs(n - 1, k) % mod


def countPartitions2(n: int, d: int, arr: List[int]) -> int:
    mod = 10 ** 9 + 7
    total = sum(arr)
    if (total - d) < 0 or (total - d) % 2:
        return 0
    k = (sum(arr) - d) // 2
    dp = [[0] * (k + 1) for _ in range(n)]

    if arr[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1
    if arr[0] != 0 and arr[0] <= k:
        dp[0][arr[0]] = 1

    for i in range(1, n):
        for cur in range(k + 1):
            not_take = dp[i - 1][cur]
            take = 0
            if arr[i] <= cur:
                take = dp[i - 1][cur - arr[i]]
            dp[i][cur] = take + not_take
    return dp[n - 1][k] % mod


"""
    s2 = total - s1
    s1 - s2 = d
    s1 - total + s1 = d
    s1 = (total - d) // 2
    
https://www.naukri.com/code360/problems/partitions-with-given-difference_3751628

Given an array ‘ARR’, partition it into two subsets (possibly empty) such that their union is the original array. 
Let the sum of the elements of these two subsets be ‘S1’ and ‘S2’.

Given a difference ‘D’, count the number of partitions in which ‘S1’ is greater than or equal to ‘S2’ and the 
difference between ‘S1’ and ‘S2’ is equal to ‘D’. Since the answer may be too large, return it modulo ‘10^9 + 7’.

If ‘Pi_Sj’ denotes the Subset ‘j’ for Partition ‘i’. Then, two partitions P1 and P2 are considered different if:

1) P1_S1 != P2_S1 i.e, at least one of the elements of P1_S1 is different from P2_S2.
2) P1_S1 == P2_S2, but the indices set represented by P1_S1 is not equal to the indices set of P2_S2. 
Here, the indices set of P1_S1 is formed by taking the indices of the elements from which the subset is formed.

Refer to the example below for clarification.
Note that the sum of the elements of an empty subset is 0.

For example :
If N = 4, D = 3, ARR = {5, 2, 5, 1}
There are only two possible partitions of this array.
Partition 1: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
Partition 2: {5, 2, 1}, {5}. The subset difference between subset sum is: (5 + 2 + 1) - (5) = 3
These two partitions are different because, in the 1st partition, S1 contains 5 from index 0, and in the 2nd 
partition, S1 contains 5 from index 2.

"""

print(countPartitions(4, 3, [5, 2, 5, 1]))
print(countPartitions(4, 3, [5, 2, 6, 4]))
print(countPartitions(4, 0, [1, 1, 1, 1]))
print(countPartitions(3, 1, [4, 6, 3]))
print(countPartitions(5, 0, [3, 1, 1, 2, 1]))
print(countPartitions(5, 1, [3, 2, 2, 5, 1]))
print(countPartitions(6, 17, [1, 0, 8, 5, 1, 4]))
print("--------------------------")
print(countPartitions2(4, 3, [5, 2, 5, 1]))
print(countPartitions2(4, 3, [5, 2, 6, 4]))
print(countPartitions2(4, 0, [1, 1, 1, 1]))
print(countPartitions2(3, 1, [4, 6, 3]))
print(countPartitions2(5, 0, [3, 1, 1, 2, 1]))
print(countPartitions2(5, 1, [3, 2, 2, 5, 1]))
print(countPartitions2(6, 17, [1, 0, 8, 5, 1, 4]))

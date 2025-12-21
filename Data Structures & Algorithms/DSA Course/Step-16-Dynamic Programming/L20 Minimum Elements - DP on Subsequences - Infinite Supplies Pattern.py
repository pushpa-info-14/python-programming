from typing import List


def minimumElements(nums: List[int], x: int) -> int:
    nums.sort()
    inf = 10 ** 10
    memo = {}

    def dfs(target):
        if target in memo:
            return memo[target]
        if target == 0:
            return 0
        cur = inf
        for num in nums:
            if num > target:
                break
            cur = min(cur, 1 + dfs(target - num))
        memo[target] = cur
        return memo[target]

    res = dfs(x)
    return res if res != inf else -1


def minimumElements2(nums: List[int], x: int) -> int:
    nums.sort()
    inf = 10 ** 10
    dp = [inf] * (x + 1)
    dp[0] = 0
    for target in range(1, x + 1):
        cur = inf
        for num in nums:
            if num > target:
                break
            cur = min(cur, 1 + dp[target - num])
        dp[target] = cur
    res = dp[x]
    return res if res != inf else -1


"""
https://www.naukri.com/code360/problems/minimum-elements_3843091

You are given an array of ‘N’ distinct integers and an integer ‘X’ representing the target sum. You have to 
tell the minimum number of elements you have to take to reach the target sum ‘X’.

Note:
You have an infinite number of elements of each type.
For example
If N=3 and X=7 and array elements are [1,2,3]. 
Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.
Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
Hence the output is 3.
"""

print(minimumElements([1, 2, 3], 7))
print(minimumElements([1], 0))
print(minimumElements([12, 1, 3], 4))
print(minimumElements([2, 1], 11))
print("-------------------")
print(minimumElements2([1, 2, 3], 7))
print(minimumElements2([1], 0))
print(minimumElements2([12, 1, 3], 4))
print(minimumElements2([2, 1], 11))

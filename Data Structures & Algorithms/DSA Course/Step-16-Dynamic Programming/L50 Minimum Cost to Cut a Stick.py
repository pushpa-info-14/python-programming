from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        inf = 10 ** 10
        memo = {}

        def dfs(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            stick_length = cuts[j + 1] - cuts[i - 1]
            res = inf
            for k in range(i, j + 1):
                res = min(res, stick_length + dfs(i, k - 1) + dfs(k + 1, j))
            memo[(i, j)] = res
            return res

        return dfs(1, len(cuts) - 2)


# LeetCode 1547
s = Solution()
print(s.minCost(n=7, cuts=[1, 3, 4, 5]))
print(s.minCost(n=9, cuts=[5, 6, 1, 4, 2]))

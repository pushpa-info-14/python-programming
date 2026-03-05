from functools import cache


class Solution:
    def minCost(self, n: int) -> int:
        @cache
        def dfs(x):
            if x == 1:
                return 0
            return (x - 1) + dfs(x - 1)

        return dfs(n)

    def minCost2(self, n: int) -> int:
        # 4 = 3 + 2 + 1
        # sn = (a1 + an) * n / 2
        # sn = (1 + n - 1) * (n - 1) / 2
        # sn = n * (n - 1) / 2
        return n * (n - 1) // 2


s = Solution()
print(s.minCost(3))
print(s.minCost(4))
print("----------------")
print(s.minCost2(3))
print(s.minCost2(4))

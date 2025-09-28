from functools import cache


class Solution:
    def soupServings(self, n: int) -> float:

        @cache
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1.0
            elif b <= 0:
                return 0
            return 0.25 * (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b - 50) + dfs(a - 25, b - 75))

        n = min(n, 5000)
        return dfs(n, n)


s = Solution()
print(s.soupServings(50))
print(s.soupServings(100))
print(s.soupServings(5000))

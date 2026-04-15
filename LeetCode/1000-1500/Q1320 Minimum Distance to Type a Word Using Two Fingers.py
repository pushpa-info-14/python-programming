from functools import cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        inf = 10 ** 10
        n = len(word)

        @cache
        def dfs(i, f1, f2):
            if i == n:
                return 0
            c = word[i]
            pos = ord(c) - ord("A")
            x, y = pos // 6, pos % 6

            cur = inf
            d1 = 0 if f1 == (-1, -1) else abs(f1[0] - x) + abs(f1[1] - y)
            cur = min(cur, d1 + dfs(i + 1, (x, y), f2))

            d2 = 0 if f2 == (-1, -1) else abs(f2[0] - x) + abs(f2[1] - y)
            cur = min(cur, d2 + dfs(i + 1, f1, (x, y)))
            return cur

        return dfs(0, (-1, -1), (-1, -1))


s = Solution()
print(s.minimumDistance(word="CAKE"))
print(s.minimumDistance(word="HAPPY"))

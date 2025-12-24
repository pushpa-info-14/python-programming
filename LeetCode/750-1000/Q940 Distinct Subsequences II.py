from functools import cache


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        mod = 10 ** 9 + 7

        @cache
        def dfs(index):
            if index == n:
                return 1
            r = 2 * dfs(index + 1)

            for i in range(index + 1, n):
                if s[index] == s[i]:
                    r -= dfs(i + 1)
                    break
            return r % mod

        return (dfs(0) - 1) % mod

    def distinctSubseqII2(self, s: str) -> int:
        n = len(s)
        mod = 10 ** 9 + 7
        prev = [-1] * n
        last = {}
        for i in range(n - 1, -1, -1):
            if s[i] in last:
                prev[i] = last[s[i]]
            last[s[i]] = i

        @cache
        def dfs(index):
            if index == n:
                return 1
            r = 2 * dfs(index + 1)

            if prev[index] != -1:
                r -= dfs(prev[index] + 1)
            return r % mod

        return (dfs(0) - 1) % mod


s = Solution()
print(s.distinctSubseqII(s="abc"))
print(s.distinctSubseqII(s="aba"))
print(s.distinctSubseqII(s="aaa"))
print("------------")
print(s.distinctSubseqII2(s="abc"))
print(s.distinctSubseqII2(s="aba"))
print(s.distinctSubseqII2(s="aaa"))

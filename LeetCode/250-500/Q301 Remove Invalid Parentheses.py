from functools import cache


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        res = []

        @cache
        def dfs(i, cur, diff):
            if diff < 0:
                return
            if i == n:
                if diff == 0:
                    res.append(cur)
                return
            if s[i] not in "()":
                dfs(i + 1, cur + s[i], diff)
            else:
                dfs(i + 1, cur + s[i], diff + (1 if s[i] == '(' else -1))
                dfs(i + 1, cur, diff)

        dfs(0, '', 0)
        mx = max(len(x) for x in res)
        return [x for x in res if len(x) == mx]


s = Solution()
print(s.removeInvalidParentheses(s="()())()"))
print(s.removeInvalidParentheses(s="(a)())()"))
print(s.removeInvalidParentheses(s=")("))

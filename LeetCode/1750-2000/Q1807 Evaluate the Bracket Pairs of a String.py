from collections import defaultdict


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = defaultdict(lambda: '?')
        for key, value in knowledge:
            mp[key] = value
        n = len(s)
        res = ''
        i = 0
        while i < n:
            if s[i] == '(':
                j = i + 1
                while s[j] != ')':
                    j += 1
                res += mp[s[i + 1:j]]
                i = j + 1
            else:
                res += s[i]
                i += 1
        return res


s = Solution()
print(s.evaluate(s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]]))
print(s.evaluate(s="hi(name)", knowledge=[["a", "b"]]))
print(s.evaluate(s="(a)(a)(a)aaa", knowledge=[["a", "yes"]]))

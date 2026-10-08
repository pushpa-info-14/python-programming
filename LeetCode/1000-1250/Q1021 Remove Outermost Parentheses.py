class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        res = []
        i = 0
        while i < n:
            diff = 1
            i += 1
            while diff > 0:
                res.append(s[i])
                diff += 1 if s[i] == '(' else -1
                i += 1
            res.pop()
        return "".join(res)


s = Solution()
print(s.removeOuterParentheses(s="(()())(())"))
print(s.removeOuterParentheses(s="(()())(())(()(()))"))
print(s.removeOuterParentheses(s="()()"))

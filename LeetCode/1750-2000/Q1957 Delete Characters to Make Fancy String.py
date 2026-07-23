class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)

        if n < 3:
            return s

        res = s[0]
        for i in range(1, n - 1):
            if s[i - 1] == s[i] == s[i + 1]:
                continue
            else:
                res += s[i]
        return res + s[n - 1]


s = Solution()
print(s.makeFancyString(s="leeetcode"))
print(s.makeFancyString(s="aaabaaaa"))
print(s.makeFancyString(s="aa"))
print(s.makeFancyString(s="a"))

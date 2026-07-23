class Solution:
    def checkString(self, s: str) -> bool:
        a_count = s.count('a')
        for c in s:
            if c == 'a':
                a_count -= 1
            else:
                return a_count == 0
        return a_count == 0


s = Solution()
print(s.checkString(s="aaa"))
print(s.checkString(s="aaabbb"))
print(s.checkString(s="abab"))
print(s.checkString(s="bbb"))

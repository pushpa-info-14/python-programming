class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 0
        prev = ""
        for c in word:
            if c == prev:
                res += 1
            else:
                prev = c
        return res + 1


s = Solution()
print(s.possibleStringCount(word="abbcccc"))
print(s.possibleStringCount(word="abcd"))
print(s.possibleStringCount(word="aaaa"))

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)
        return ''


s = Solution()
print(s.repeatedCharacter(s="abccbaacz"))
print(s.repeatedCharacter(s="abcdd"))

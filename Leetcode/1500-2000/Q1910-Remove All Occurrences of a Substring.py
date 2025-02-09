class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if s.find(part) < 0:
            return s
        new_s = s.replace(part, "", 1)
        return self.removeOccurrences(new_s, part)


s = Solution()
print(s.removeOccurrences("daabcbaabcbc", "abc"))
print(s.removeOccurrences("axxxxyyyyb", "xy"))
print(s.removeOccurrences("aabababa", "aba"))

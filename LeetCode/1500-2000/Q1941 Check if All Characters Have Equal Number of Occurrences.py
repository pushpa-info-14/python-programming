from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        prev = counter[s[0]]
        for c in s:
            if counter[c] != prev:
                return False
        return True


s = Solution()
print(s.areOccurrencesEqual(s="abacbc"))
print(s.areOccurrencesEqual(s="aaabb"))

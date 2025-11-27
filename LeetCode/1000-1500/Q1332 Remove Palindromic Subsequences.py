from collections import Counter


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        counter = Counter(s)
        return len(counter.keys())


s = Solution()
print(s.removePalindromeSub(s="ababa"))
print(s.removePalindromeSub(s="abb"))
print(s.removePalindromeSub(s="baabb"))

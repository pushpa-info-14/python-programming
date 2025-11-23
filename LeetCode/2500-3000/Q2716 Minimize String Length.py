class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))


s = Solution()
print(s.minimizedStringLength(s="aaabc"))
print(s.minimizedStringLength(s="cbbd"))
print(s.minimizedStringLength(s="baadccab"))

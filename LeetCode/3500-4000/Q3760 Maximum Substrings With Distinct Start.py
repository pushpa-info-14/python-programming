class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))


s = Solution()
print(s.maxDistinct(s="abab"))
print(s.maxDistinct(s="abcd"))
print(s.maxDistinct(s="aaaa"))

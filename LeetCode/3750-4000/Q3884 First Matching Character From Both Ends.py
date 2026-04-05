class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        l, r = 0, n - 1
        while l <= r:
            if s[l] == s[r]:
                return l
            l += 1
            r -= 1
        return -1


s = Solution()
print(s.firstMatchingIndex(s="abcacbd"))
print(s.firstMatchingIndex(s="abc"))
print(s.firstMatchingIndex(s="abcdab"))

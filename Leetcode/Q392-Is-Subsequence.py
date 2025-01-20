class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        l = 0
        i = 0
        while i < len(t) and l < len(s):
            if s[l] == t[i]:
                l += 1
            i += 1
        if l == len(s):
            return True
        return False


s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdc"))

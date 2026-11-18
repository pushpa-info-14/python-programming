class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                res += 1
        return res


s = Solution()
print(s.minChanges(s="1001"))
print(s.minChanges(s="10"))
print(s.minChanges(s="0000"))

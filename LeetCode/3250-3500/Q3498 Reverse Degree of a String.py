class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (i + 1) * (123 - ord(s[i]))
        return res


s = Solution()
print(s.reverseDegree(s="abc"))
print(s.reverseDegree(s="zaza"))

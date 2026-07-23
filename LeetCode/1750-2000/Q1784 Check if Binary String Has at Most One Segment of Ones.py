class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ones = s.count('1')
        a = s.lstrip('1')
        return ones == len(s) - len(a)


s = Solution()
print(s.checkOnesSegment(s="1001"))
print(s.checkOnesSegment(s="110"))

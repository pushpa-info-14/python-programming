class Solution:
    def generateTheString(self, n: int) -> str:
        if n & 1:
            return 'a' * n
        else:
            return 'a' * (n - 1) + 'b'


s = Solution()
print(s.generateTheString(4))
print(s.generateTheString(2))
print(s.generateTheString(7))

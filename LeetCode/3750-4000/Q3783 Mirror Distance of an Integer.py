class Solution:
    def mirrorDistance(self, n: int) -> int:
        x = n
        num = 0
        while x:
            digit = x % 10
            x //= 10
            num = num * 10 + digit
        return abs(n - num)


s = Solution()
print(s.mirrorDistance(25))
print(s.mirrorDistance(10))
print(s.mirrorDistance(7))

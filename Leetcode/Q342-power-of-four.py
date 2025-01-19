class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False

        while n:
            if n == 1:
                return True
            if n % 4 != 0:
                return False
            n = n // 4

        return True


s = Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(5))
print(s.isPowerOfFour(1))
print(s.isPowerOfFour(9))

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False

        while n:
            if n == 1:
                return True
            if n % 3 != 0:
                return False
            n = n // 3

        return True


s = Solution()
print(s.isPowerOfThree(27))
print(s.isPowerOfThree(0))
print(s.isPowerOfThree(-1))
print(s.isPowerOfThree(9))

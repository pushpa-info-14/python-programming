class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = -1
        while n:
            bit = n % 2
            n //= 2
            if bit == prev:
                return False
            prev = bit
        return True


s = Solution()
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
print(s.hasAlternatingBits(11))

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        res = 0
        pos = 0
        while n:
            bit = n % 2
            bit = 1 if bit == 0 else 0
            res |= bit << pos
            pos += 1
            n //= 2
        return res


s = Solution()
print(s.bitwiseComplement(5))
print(s.bitwiseComplement(7))
print(s.bitwiseComplement(10))

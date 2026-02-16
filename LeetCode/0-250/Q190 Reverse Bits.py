class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res

    def reverseBits2(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            res |= (n % 2)
            n >>= 1
        return res


s = Solution()
print(s.reverseBits(43261596))
print(s.reverseBits(2147483644))
print("-----------------")
print(s.reverseBits2(43261596))
print(s.reverseBits2(2147483644))

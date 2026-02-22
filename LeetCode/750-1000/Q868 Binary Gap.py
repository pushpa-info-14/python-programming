class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        set_bits = 0
        count = 0
        while n:
            count += 1
            if n % 2:
                set_bits += 1
                if set_bits > 1:
                    res = max(res, count)
                count = 0
            n >>= 1
        return res


s = Solution()
print(s.binaryGap(22))
print(s.binaryGap(8))
print(s.binaryGap(5))

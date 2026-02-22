class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        cur = -1000
        while n:
            cur += 1
            if n % 2:
                res = max(res, cur)
                cur = 0
            n >>= 1
        return res


s = Solution()
print(s.binaryGap(22))
print(s.binaryGap(8))
print(s.binaryGap(5))

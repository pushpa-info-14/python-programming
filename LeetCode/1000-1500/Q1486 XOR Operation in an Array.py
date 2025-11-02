class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res


s = Solution()
print(s.xorOperation(n=5, start=0))
print(s.xorOperation(n=4, start=3))

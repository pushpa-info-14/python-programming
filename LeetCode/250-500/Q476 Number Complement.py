class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        n = 0
        while num:
            bit = 0 if num & 1 else 1
            res = res | bit << n
            n += 1
            num = num >> 1
        return res


s = Solution()
print(s.findComplement(5))
print(s.findComplement(1))

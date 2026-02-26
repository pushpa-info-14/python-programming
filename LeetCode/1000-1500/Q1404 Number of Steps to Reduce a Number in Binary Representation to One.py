class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        res = 0
        while num > 1:
            res += 1
            if num & 1:
                num += 1
            else:
                num //= 2
        return res


s = Solution()
print(s.numSteps(s="1101"))
print(s.numSteps(s="10"))
print(s.numSteps(s="1"))

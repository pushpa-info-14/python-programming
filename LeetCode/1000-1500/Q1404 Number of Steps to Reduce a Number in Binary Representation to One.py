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

    def numSteps2(self, s: str) -> int:
        res = 0
        carry = 0
        for i in reversed(range(1, len(s))):
            bit = int(s[i]) + carry
            if bit % 2:
                res += 2
                carry = 1
            else:
                res += 1
        return res + carry


s = Solution()
print(s.numSteps(s="1101"))
print(s.numSteps(s="10"))
print(s.numSteps(s="1"))
print("--------------")
print(s.numSteps2(s="1101"))
print(s.numSteps2(s="10"))
print(s.numSteps2(s="1"))

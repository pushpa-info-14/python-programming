class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num //= 2
            res += 1
        return res


s = Solution()
print(s.numberOfSteps(14))
print(s.numberOfSteps(8))
print(s.numberOfSteps(123))

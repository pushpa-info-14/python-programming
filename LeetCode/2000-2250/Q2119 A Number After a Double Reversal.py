class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return True if num % 10 else False


s = Solution()
print(s.isSameAfterReversals(526))
print(s.isSameAfterReversals(1800))
print(s.isSameAfterReversals(0))

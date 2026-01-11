class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        digits = list(num)
        while digits[-1] == '0':
            digits.pop()
        return "".join(digits)

    def removeTrailingZeros2(self, num: str) -> str:
        return num.rstrip('0')


s = Solution()
print(s.removeTrailingZeros(num="51230100"))
print(s.removeTrailingZeros(num="123"))
print(s.removeTrailingZeros2(num="51230100"))
print(s.removeTrailingZeros2(num="123"))

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        digits.sort()
        return digits[0] * 10 + digits[1] * 10 + digits[2] + digits[3]


s = Solution()
print(s.minimumSum(2932))
print(s.minimumSum(4009))

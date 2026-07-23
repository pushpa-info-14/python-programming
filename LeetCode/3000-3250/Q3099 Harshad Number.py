class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = 0
        num = x
        while num:
            digit_sum += num % 10
            num //= 10
        return digit_sum if x % digit_sum == 0 else -1


s = Solution()
print(s.sumOfTheDigitsOfHarshadNumber(18))
print(s.sumOfTheDigitsOfHarshadNumber(23))

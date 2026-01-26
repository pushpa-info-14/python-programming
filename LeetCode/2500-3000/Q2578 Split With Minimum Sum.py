class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        digits.sort()
        num1, num2 = 0, 0
        flag = True
        for digit in digits:
            if flag:
                num1 = num1 * 10 + digit
            else:
                num2 = num2 * 10 + digit
            flag = not flag
        return num1 + num2


s = Solution()
print(s.splitNum(4325))
print(s.splitNum(687))

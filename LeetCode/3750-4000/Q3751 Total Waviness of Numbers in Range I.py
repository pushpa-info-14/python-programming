class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for num in range(num1, num2 + 1):
            digits = []
            while num:
                digits.append(num % 10)
                num //= 10
            if len(digits) < 3:
                continue
            for i in range(1, len(digits) - 1):
                if digits[i - 1] < digits[i] > digits[i + 1]:
                    res += 1
                elif digits[i - 1] > digits[i] < digits[i + 1]:
                    res += 1
        return res


s = Solution()
print(s.totalWaviness(num1=120, num2=130))
print(s.totalWaviness(num1=198, num2=202))
print(s.totalWaviness(num1=4848, num2=4848))

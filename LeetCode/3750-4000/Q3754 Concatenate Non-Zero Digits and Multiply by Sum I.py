class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0: return 0
        x = ''
        total = 0
        while n:
            digit = n % 10
            n //= 10
            total += digit
            if digit:
                x += str(digit)
        return int(x[::-1]) * total


s = Solution()
print(s.sumAndMultiply(10203004))
print(s.sumAndMultiply(1000))
print(s.sumAndMultiply(0))

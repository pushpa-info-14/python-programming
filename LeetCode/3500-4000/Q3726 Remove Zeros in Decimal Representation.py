class Solution:
    def removeZeros(self, n: int) -> int:
        res = 0
        digits = []
        while n:
            digit = n % 10
            if digit:
                digits.append(digit)
            n //= 10
        digits.reverse()
        for x in digits:
            res *= 10
            res += x
        return res


s = Solution()
print(s.removeZeros(n=1020030))
print(s.removeZeros(n=1))

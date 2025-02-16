class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        sign = True
        if dividend >= 0 and divisor < 0:
            sign = False
        elif dividend <= 0 and divisor > 0:
            sign = False

        n = abs(dividend)
        d = abs(divisor)
        res = 0
        while n >= d:
            count = 0
            while n >= (d << (count + 1)):
                count += 1
            res += (1 << count)
            n -= (d << count)

        int_max = 1 << 31
        if res == int_max and sign:
            return int_max - 1
        if res == int_max and not sign:
            return -int_max
        return res if sign else -res


s = Solution()
print(s.divide(10, 3))
print(s.divide(7, -3))
print(s.divide(1, 1))
print(s.divide(-2147483648, -1))
print(s.divide(2147483647, 3))

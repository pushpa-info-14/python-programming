class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []
        seen_at = {}
        sign = ''
        if numerator < 0 < denominator or numerator > 0 > denominator:
            sign = '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        recurring_at = -1
        full = numerator // denominator
        numerator %= denominator
        seen_at[numerator] = len(res)
        numerator *= 10

        while numerator != 0:
            res.append(str(numerator // denominator))
            numerator %= denominator
            if numerator in seen_at:
                recurring_at = seen_at[numerator]
                break
            else:
                seen_at[numerator] = len(res)
            numerator *= 10

        if recurring_at == -1:
            if res:
                return f"{sign}{full}." + ''.join(res)
            else:
                return f"{sign}{full}"
        else:
            return f"{sign}{full}.{''.join(res[:recurring_at])}({''.join(res[recurring_at:])})"


s = Solution()
print(s.fractionToDecimal(numerator=1, denominator=2))
print(s.fractionToDecimal(numerator=2, denominator=1))
print(s.fractionToDecimal(numerator=4, denominator=333))
print(s.fractionToDecimal(numerator=22, denominator=7))
print(s.fractionToDecimal(numerator=20, denominator=3))
print(s.fractionToDecimal(numerator=-20, denominator=3))
print(s.fractionToDecimal(numerator=50, denominator=8))
print(s.fractionToDecimal(numerator=-50, denominator=8))

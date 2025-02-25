def divide(dividend, divisor):
    if dividend == divisor: return 1

    sign = True
    if dividend >= 0 > divisor: sign = False
    if dividend < 0 < divisor: sign = False

    n = abs(dividend)
    d = abs(divisor)
    res = 0
    while n >= d:
        count = 0
        while n >= d << (count + 1):
            count += 1
        res += 1 << count
        n = n - d * (1 << count)
    int_max = 1 << 31
    if res >= int_max and sign:
        return int_max - 1
    if res >= int_max and not sign:
        return -int_max
    return res if sign else -res


print(divide(10, 2))
print(divide(-10, 2))
print(divide(-10, -2))
print(divide(10, -2))

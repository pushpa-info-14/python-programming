def pow(x, n):
    m = n
    n = abs(n)
    ans = 1
    while n:
        if n & 1:
            ans *= x
        x *= x
        n //= 2

    if m < 0:
        return 1.0 / ans
    return ans


print(pow(2, 5))
print(pow(2, -5))

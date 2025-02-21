def pow(x, n):
    m = n
    n = abs(n)
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans = ans * x
            n = n - 1
        else:
            n = n / 2
            x = x * x

    if m < 0:
        return 1.0 / ans
    return ans


print(pow(2, 5))
print(pow(2, -5))

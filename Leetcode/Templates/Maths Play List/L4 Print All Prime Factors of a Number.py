def prime_factors(n):
    res = []
    i = 2
    while i < n ** 0.5:
        if n % i == 0:
            res.append(i)
            while n % i == 0:
                n = n // i
        i += 1

    if n != 1:
        res.append(n)
    return res


print(prime_factors(60))
print(prime_factors(780))
print(prime_factors(37))

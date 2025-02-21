def print_divisors(n):
    res = []
    for i in range(1, int(n * .5) + 1):
        if n % i == 0:
            res.append(i)
            if n // i != i:
                res.append(n // i)
    res.sort()
    print(res)

print_divisors(36)
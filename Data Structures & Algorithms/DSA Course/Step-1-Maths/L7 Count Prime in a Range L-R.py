def get_sieve(n):
    primes = [1] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i] == 1:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return primes


def count_primes(queries):
    primes = get_sieve(10 ** 6)
    cnt = 0
    for i in range(2, 10 ** 6 + 1):
        cnt = cnt + primes[i]
        primes[i] = cnt

    for l, r in queries:
        print(primes[r] - primes[l - 1])


count_primes([[1, 10], [1, 20], [1, 100], [1000, 5000]])

from typing import List


def prime_factors(queries: List[int]):
    spf = [i for i in range(10 ** 5 + 1)]

    for i in range(2, 10 ** 5 + 1):
        if spf[i] == i:
            for j in range(i * i, 10 ** 5 + 1, i):
                if spf[j] == j:
                    spf[j] = i

    for n in queries:
        res = []
        while n != 1:
            res.append(spf[n])
            n = n // spf[n]
        print(res)


prime_factors([11, 20, 50, 125])

def matrix_multiply(a, b):
    n = len(a)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j]
    return res


def calculate(a, n):
    size = len(a[0])
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        res[i][i] = 1

    while n:
        if n & 1:
            res = matrix_multiply(a, res)
        a = matrix_multiply(a, a)
        n //= 2

    return res


print(calculate([[2, 3],[1, 2]], 1))
print(calculate([[2, 3],[1, 2]], 5))
print(calculate([[1, 3], [3, 2]], 10))

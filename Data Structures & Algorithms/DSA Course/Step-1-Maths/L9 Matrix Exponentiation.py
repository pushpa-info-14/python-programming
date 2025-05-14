def matrix_multiply_original(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise ValueError("Cannot multiply: number of columns in a must be equal to number of rows in b.")

    res = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):  # Iterate through rows of matrix a
        for j in range(cols_b):  # Iterate through columns of matrix b
            for k in range(cols_a):  # Iterate through columns of matrix a
                res[i][j] += a[i][k] * b[k][j]
    return res


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


# Exponentiation will work only on square matrix
print(calculate([[2, 3], [1, 2]], 1))
print(calculate([[2, 3, 7], [1, 2, 4], [1, 1, 8]], 10))
print(calculate([[2, 3], [1, 2]], 5))
print(calculate([[1, 3], [3, 2]], 10))

def rotate(matrix):
    n = len(matrix)
    res = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            res[j][n - 1 - i] = matrix[i][j]
    return res


def rotate2(matrix):
    n = len(matrix)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        l, r = 0, n - 1
        while l < r:
            matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1
    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

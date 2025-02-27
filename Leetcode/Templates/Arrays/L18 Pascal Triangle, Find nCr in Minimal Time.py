def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


# r-1Cc-1
# 7C2 = 7x6x5!/2x1x5!
# 7x6 2x1
# 7/1 7x6/1x2

def pascalNumber(row, col):
    return nCr(row - 1, col - 1)


def pascalRow(row):
    res = []
    for col in range(1, row + 1):
        res.append(nCr(row - 1, col - 1))
    return res


def pascalRow2(row):
    res = []
    ans = 1
    res.append(ans)
    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // col
        res.append(ans)
    return res


def pascalTriangle(n):
    res = []
    for row in range(1, n + 1):
        res.append(pascalRow2(row))
    return res


print(pascalNumber(5, 3))
print(pascalRow(6))
print(pascalRow2(6))
print(pascalTriangle(6))

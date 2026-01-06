"""
https://www.naukri.com/code360/problems/matrix-chain-multiplication_975344

Given a chain of matrices A1, A2, A3,.....An. Your task is to find out the minimum cost to multiply these matrices.
The cost of matrix multiplication is defined as the number of scalar multiplications. A Chain of
matrices A1, A2, A3,.....An is represented by a sequence of numbers in an array ‘arr’ where the dimension of 1st
matrix is equal to arr[0] * arr[1] , 2nd matrix is arr[1] * arr[2], and so on.

For example:
For arr[ ] = { 10, 20, 30, 40}, matrix A1 = [10 * 20], A2 = [20 * 30], A3 = [30 * 40]

Scalar multiplication of matrix with dimension 10 * 20 is equal to 200.
"""


def matrixMultiplication(arr, n):
    inf = 10 ** 10
    dp = [[inf] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n):
            res = inf
            for k in range(i, j):
                res = min(res, arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][j])
            dp[i][j] = res

    return dp[1][n - 1]


print(matrixMultiplication([4, 5, 3, 2], 4))
print(matrixMultiplication([10, 15, 20, 25], 4))

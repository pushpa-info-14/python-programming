"""
You are given an expression 'exp' in the form of a string where operands will be : (TRUE or FALSE), and
operators will be : (AND, OR or XOR).

Now you have to find the number of ways we can parenthesize the expression such that it will evaluate to TRUE.

As the answer can be very large, return the output modulo 1000000007.

Note :

‘T’ will represent the operand TRUE.
‘F’ will represent the operand FALSE.
‘|’ will represent the operator OR.
‘&’ will represent the operator AND.
‘^’ will represent the operator XOR.
Example :

Input: 'exp’ = "T|T & F".

Output: 1

Explanation:
There are total 2  ways to parenthesize this expression:
    (i) (T | T) & (F) = F
    (ii) (T) | (T & F) = T
Out of 2 ways, one will result in True, so we will return 1.
"""


def evaluateExp(exp: str) -> int:
    mod = 10 ** 9 + 7
    n = len(exp)
    memo = {}

    def dfs(i, j, is_true):
        if i == j:
            if is_true:
                return 1 if exp[i] == "T" else 0
            else:
                return 1 if exp[i] == "F" else 0
        if (i, j, is_true) in memo:
            return memo[(i, j, is_true)]

        ways = 0
        for k in range(i + 1, j, 2):
            operand = exp[k]
            lt = dfs(i, k - 1, True)
            lf = dfs(i, k - 1, False)
            rt = dfs(k + 1, j, True)
            rf = dfs(k + 1, j, False)
            if operand == "|":
                if is_true:
                    ways += lt * rt + lt * rf + lf * rt
                else:
                    ways += lf * rf
            elif operand == "&":
                if is_true:
                    ways += lt * rt
                else:
                    ways += lt * rf + lf * rt + lf * rf
            elif operand == "^":
                if is_true:
                    ways += lt * rf + lf * rt
                else:
                    ways += lt * rt + lf * rf
        ways %= mod
        memo[(i, j, is_true)] = ways
        return ways

    return dfs(0, n - 1, True)


print(evaluateExp("T|T&F"))  # 1
print(evaluateExp("T^T^F"))  # 0
print(evaluateExp("F|T^F"))  # 2
print(evaluateExp(
    "F^F^F^F&T|T|F|T|F|F|T|T|T|T&T|T|T&T|F&T|F|T|T|T^T|F^T|T&F^T|F|T|F|T&T|T^F|F^T&T^T&T^T&T^T&F&T^F|F^T|T|F|F^F|F&F|F|T&F&F"))

"""
Given an integer n, return an array ans of length n +1 such that for each i (0 <= i <= n), ans[i] is
the number of 1's in the binary representation of i.

Example 1:
    Input: n = n = 2
    Output: [0,1,1]
    Explanation:
        0 --> 0 --> 0
        1 --> 1 --> 1
        2 --> 10 --> 1
"""


def counting_bits(n):
    res = [0] * (n + 1)
    offset = 1
    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        res[i] = 1 + res[i - offset]
    return res


print(counting_bits(2))
print(counting_bits(15))

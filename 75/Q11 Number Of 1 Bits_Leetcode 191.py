"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has.
Also known as the Hamming weight.

Example 1:
    Input: n = 00000000000000000000000000001011
    Output: 3
"""


def hamming_weight1(n):
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res


def hamming_weight2(n):
    res = 0
    while n:
        n &= (n - 1)
        res += 1
    return res


print(hamming_weight1(3))
print(hamming_weight1(15))
print(hamming_weight2(3))
print(hamming_weight2(15))

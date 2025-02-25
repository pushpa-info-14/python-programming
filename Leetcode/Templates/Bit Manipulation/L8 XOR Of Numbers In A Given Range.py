def xor_1_to_n(n):
    if n % 4 == 1: return 1
    if n % 4 == 2: return n + 1
    if n % 4 == 3: return 0
    return n


def xor_range(l, r):
    return xor_1_to_n(l - 1) ^ xor_1_to_n(r)


print(xor_range(5, 10))
print(xor_range(520, 5000))
print(xor_range(520, 5001))

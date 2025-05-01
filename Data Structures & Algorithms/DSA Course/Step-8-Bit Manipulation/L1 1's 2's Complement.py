def num_to_binary(n):
    res = ""

    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return res


def binary_to_num(binary):
    res = 0
    n = 1
    for i in reversed(range(len(binary))):
        res += int(binary[i]) * n
        n *= 2
    return res


print(num_to_binary(2))
print(num_to_binary(3))
print(num_to_binary(4))
print(num_to_binary(5))

print(binary_to_num("10"))
print(binary_to_num("11"))
print(binary_to_num("100"))
print(binary_to_num("101"))

"""
1's compliment
101 ---> 010 (Flip bits)

2's compliment
101 ---> 010 + 1 --> 011 (1's compliment + 1)

AND(&)
all true    -> true
1 false     -> false

OR(|)
1 true      -> true
all false   -> false

XOR(^)
number of 1s are odd    -> true
number of 1s are even   -> false

>>
13 = 1101
13 >> 1 = 110   = 6 = 13 // 2
13 >> 2 =  11   = 3 = 13 // 4
13 >> 4 =   0   = 0 = 13 // 16

<<
2 = 10
2 << 3 = 10000 = 16 = 2 x 16

NOT(~)

1. Flip
2. Check negative
    2's compliment if negative

=====================================  
x = ~6

000000000000101 1.Flip bits
111111111111010 2.Negative number
100000000000101 3.Convert to 2's complement
             +1
100.........110
x = -6

=====================================
x = ~(-6)

000000000000110
111111111111001
             +1
111111111111010 2's compliment
000000000000101 Flip bits
x = 5
"""

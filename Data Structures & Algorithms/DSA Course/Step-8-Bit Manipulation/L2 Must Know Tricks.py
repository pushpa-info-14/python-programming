# 1. Swap two numbers

a = 5
b = 7
a = a ^ b
b = a ^ b  # a ^ b ^ b = a
a = a ^ b  # a ^ b ^ a = b

print(a, b)


# 2. Check if the ith bit is set or not

def is_set1(n, i):
    return n & 1 << i


def is_set2(n, i):
    return n >> i & 1


print(is_set1(13, 0))
print(is_set1(13, 1))
print(is_set2(13, 0))
print(is_set2(13, 1))


# 3. Set the ith bit

def set_bit(n, i):
    return n | 1 << i


print(set_bit(13, 1))
print(set_bit(13, 2))


# 4. Clear the ith bit

def clear_bit(n, i):
    return n & ~(1 << i)


print(clear_bit(13, 2))


# 5. Toggle the ith bit

def toggle_bit(n, i):
    return n ^ 1 << i


print(toggle_bit(13, 1))


# 6. Remove the last set bit(right most)
# 16      = 10000
# 15      = 01111
# 16 & 15 = 00000

def remove_last_set_bit(n):
    return n & n - 1


print(remove_last_set_bit(12))


# 7. Check if the number is a power of 2

def check_num(n):
    return True if n & n - 1 == 0 else False


print(check_num(13))
print(check_num(4))


# 8. Count the number of set bits

def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n = n >> 1
    return count


def count_bits2(n):
    count = 0
    while n:
        count += 1
        n = n & n - 1
    return count


print(count_bits(13))
print(count_bits(4))
print(count_bits2(13))
print(count_bits2(4))

def min_flips(num1, num2):
    num = num1 ^ num2
    count = 0
    while num:
        count += 1
        num = num & num - 1
    return count


print(min_flips(3, 4))
print(min_flips(10, 7))

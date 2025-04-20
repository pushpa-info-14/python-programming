def find_sqrt(num: int):
    res = 1
    low, high = 1, num
    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= num:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res


print(find_sqrt(25))
print(find_sqrt(27))
print(find_sqrt(7))
print(find_sqrt(1000000))

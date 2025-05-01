def nth_root(n: int, num: int):
    low, high = 1, num
    while low <= high:
        mid = (low + high) // 2
        nth_power = mid ** n
        if nth_power == num:
            return mid
        elif nth_power < num:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(nth_root(3, 27))
print(nth_root(4, 69))
print(nth_root(9, 1953125))

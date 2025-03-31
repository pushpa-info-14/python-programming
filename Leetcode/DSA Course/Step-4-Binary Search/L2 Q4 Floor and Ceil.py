def find_floor(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res


def find_ceil(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    res = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res


# Floor - Largest number in array <= x
# Ceil - Smallest number in array >= x (Lower bound)
print(find_floor([10, 20, 30, 40, 50], 25))
print(find_ceil([10, 20, 30, 40, 50], 25))
print(find_floor([10, 20, 25, 30, 40, 50], 25))
print(find_ceil([10, 20, 25, 30, 40, 50], 25))

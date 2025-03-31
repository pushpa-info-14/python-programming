def find_iterative(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def find_recursive(nums, low, high, target):
    if high < low:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return find_recursive(nums, mid + 1, high, target)
    else:
        return find_recursive(nums, low, mid - 1, target)


def find_overflow_case(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(find_iterative([1, 2, 3, 4, 5, 67, 9, 10, 12], 12))
print(find_recursive([1, 2, 3, 4, 5, 67, 9, 10, 12], 0, 8, 12))
print(find_overflow_case([1, 2, 3, 4, 5, 67, 9, 10, 12], 12))

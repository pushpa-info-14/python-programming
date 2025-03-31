def lower_bound(nums, target):
    n = len(nums)
    res = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res


def upper_bound(nums, target):
    n = len(nums)
    res = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res


def find(nums, target):
    n = len(nums)
    lb = lower_bound(nums, target)
    if lb == n or nums[lb] != target: return [-1, -1]
    return [lb, upper_bound(nums, target) - 1]


def find2(nums, target):
    n = len(nums)
    first = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            first = mid
            high = mid - 1

    last = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            last = mid
            low = mid + 1

    return [first, last]


print(find([2, 4, 6, 8, 8, 8, 11, 13], 6))
print(find([2, 4, 6, 8, 8, 8, 11, 13], 8))
print(find([2, 4, 6, 8, 8, 8, 11, 13], 15))
print(find2([2, 4, 6, 8, 8, 8, 11, 13], 6))
print(find2([2, 4, 6, 8, 8, 8, 11, 13], 8))
print(find2([2, 4, 6, 8, 8, 8, 11, 13], 15))

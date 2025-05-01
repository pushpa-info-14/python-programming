def count_occurrences(nums, target):
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

    if first == -1:
        return 0
    return last - first + 1


print(count_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 6))
print(count_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 8))
print(count_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 15))

def find_lower_bound(nums, target):
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


print(find_lower_bound([1, 2, 3, 3, 5, 8, 8, 10, 10, 11], 3))  # Smallest index such that nums[i] >= x

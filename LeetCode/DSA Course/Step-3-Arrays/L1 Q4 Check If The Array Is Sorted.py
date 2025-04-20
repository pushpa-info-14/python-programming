def is_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            return False
    return True


print(is_sorted([1, 2, 2, 3, 3, 3, 4]))
print(is_sorted([1, 2, 1, 3, 4, 3, 4]))

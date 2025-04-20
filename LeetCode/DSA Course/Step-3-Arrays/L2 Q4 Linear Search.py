def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


print(search([1, 2, 3, 4], 4))
print(search([1, 2, 3, 4], 5))

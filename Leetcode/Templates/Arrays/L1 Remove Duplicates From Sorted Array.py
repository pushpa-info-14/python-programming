def uniqueElements(nums):
    n = len(nums)
    last = 0

    for i in range(n):
        if nums[i] != nums[last]:
            last += 1
            nums[last] = nums[i]
    return last + 1


print(uniqueElements([1, 1, 2, 2, 2, 3, 3]))

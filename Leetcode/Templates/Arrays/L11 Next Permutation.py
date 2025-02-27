def nextPermutation(nums):
    n = len(nums)
    index = -1

    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            index = i
            break
    if index == -1:
        nums.sort()
        return nums

    for i in range(n - 1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

    l, r = index + 1, n - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums


print(nextPermutation([3, 1, 2]))
print(nextPermutation([3, 2, 1]))
print(nextPermutation([2, 1, 5, 4, 3, 0, 0]))
print(nextPermutation([5, 4, 3, 2, 1, 0, 0]))

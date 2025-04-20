def rotate(nums, d):
    n = len(nums)
    d = d % n
    temp = [0] * d

    for i in range(d):
        temp[i] = nums[i]

    for i in range(d, n):
        nums[i - d] = nums[i]

    for i in range(d):
        nums[n - d + i] = temp[i]
    return nums


def reverse(nums, start, end):
    l, r = start, end
    while l <= r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1


def rotate2(nums, d):
    n = len(nums)
    d = d % n

    reverse(nums, 0, d - 1)
    reverse(nums, d, n - 1)
    reverse(nums, 0, n - 1)
    return nums


print(rotate([1, 2, 3, 4, 5, 6, 7], 1))
print(rotate([1, 2, 3, 4, 5, 6, 7], 2))
print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate2([1, 2, 3, 4, 5, 6, 7], 1))
print(rotate2([1, 2, 3, 4, 5, 6, 7], 2))
print(rotate2([1, 2, 3, 4, 5, 6, 7], 3))

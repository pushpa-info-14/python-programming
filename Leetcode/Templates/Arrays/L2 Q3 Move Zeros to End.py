def move_zeros(nums):
    n = len(nums)
    count = 0
    i = 0
    for j in range(n):
        if nums[j] == 0:
            count += 1
        else:
            nums[i] = nums[j]
            i += 1
    for i in range(count):
        nums[n - count + i] = 0
    return nums


def move_zeros2(nums):
    n = len(nums)
    zero_idx = -1
    for i in range(n):
        if nums[i] == 0:
            zero_idx = i
            break

    if zero_idx == -1:
        return nums

    for i in range(zero_idx + 1, n):
        if nums[i] != 0:
            nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
            zero_idx += 1

    return nums


print(move_zeros([1, 0, 2, 3, 2, 0, 0, 4, 5, 1]))
print(move_zeros2([1, 0, 2, 3, 2, 0, 0, 4, 5, 1]))
print(move_zeros2([1, 7, 2, 3, 2, 7, 9, 4, 5, 1]))

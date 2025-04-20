def single_number(nums):
    xor = 0
    for num in nums:
        xor ^= num

    right_most = xor ^ (xor & xor - 1)
    bucket1 = 0
    bucket2 = 0
    for num in nums:
        if num & right_most:
            bucket1 ^= num
        else:
            bucket2 ^= num

    return [bucket1, bucket2]


print(single_number([2, 4, 2, 6, 3, 7, 7, 3]))
print(single_number([2, 4, 2, 14, 3, 7, 7, 3]))

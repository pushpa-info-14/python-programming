def findNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor


print(findNumber([1, 1, 2, 3, 3, 4, 4]))

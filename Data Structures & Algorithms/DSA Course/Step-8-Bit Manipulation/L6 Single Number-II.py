def single_number(nums):
    res = 0

    for i in range(31):
        count = 0
        for num in nums:
            if num & 1 << i:
                count += 1
        if count % 3 == 1:
            res = res | 1 << i
    return res


def single_number2(nums):
    n = len(nums)
    nums.sort()

    for i in range(1, n, 3):
        if nums[i - 1] != nums[i]:
            return nums[i - 1]
    return nums[n - 1]


def single_number3(nums):
    n = len(nums)
    ones = 0
    twos = 0

    for i in range(n):
        ones = (ones ^ nums[i]) & ~twos
        twos = (twos ^ nums[i]) & ~ones
    return ones


print(single_number([4, 4, 4, 1, 2, 2, 1, 2, 1, 7]))
print(single_number2([4, 4, 4, 1, 2, 2, 1, 2, 1, 7]))
print(single_number3([4, 4, 4, 1, 2, 2, 1, 2, 1, 7]))

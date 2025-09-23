from typing import List


def single_number(nums: List[int]):
    nums_set = set(nums)
    set_sum = sum(nums_set) * 2
    current_sum = sum(nums)

    return set_sum - current_sum


def single_number2(nums: List[int]):
    xor = 0
    for num in nums:
        xor ^= num
    return xor


print(single_number([2, 2, 1]))
print(single_number([4, 1, 2, 1, 2]))
print(single_number2([2, 2, 1]))
print(single_number2([4, 1, 2, 1, 2]))

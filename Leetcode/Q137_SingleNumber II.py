from typing import List


def single_number(nums: List[int]):
    nums_set = set(nums)
    set_sum = sum(nums_set) * 3
    current_sum = sum(nums)

    return int((set_sum - current_sum)/2)


print(single_number([2, 2, 3, 2]))
print(single_number([0, 1, 0, 1, 0, 1, 99]))

from typing import List


def find_duplicate(nums: List[int]):
    nums_set = set()

    for num in nums:
        if num in nums_set:
            return num
        else:
            nums_set.add(num)


print(find_duplicate([1, 3, 4, 2, 2]))
print(find_duplicate([3, 1, 3, 4, 2]))

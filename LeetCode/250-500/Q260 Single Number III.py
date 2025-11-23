from typing import List


def single_number(nums: List[int]):
    nums.sort()
    stack = []
    prev = nums[0]
    stack.append(nums[0])
    for i in range(1, len(nums)):
        if prev == nums[i]:
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(nums[i])
            prev = nums[i]
    return stack


print(single_number([1, 2, 1, 3, 2, 5]))
print(single_number([-1, 0]))
print(single_number([0, 1]))

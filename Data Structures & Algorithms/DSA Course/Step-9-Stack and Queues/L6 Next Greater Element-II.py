from typing import List


def next_greater_element(nums: List[int]):
    n = len(nums)
    res = [-1] * n
    stack = []

    i = 2 * n - 1
    while i >= 0:
        index = i % n
        while stack and stack[-1] <= nums[index]:
            stack.pop()
        if stack:
            res[index] = stack[-1]
        stack.append(nums[index])
        i -= 1
    return res


print(next_greater_element([2, 10, 12, 1, 11]))

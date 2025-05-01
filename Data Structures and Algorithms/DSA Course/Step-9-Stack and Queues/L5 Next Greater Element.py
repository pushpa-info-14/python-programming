from typing import List


def next_greater_element(nums: List[int]):
    n = len(nums)
    res = [-1] * n
    stack = []

    i = n - 1
    while i >= 0:
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])
        i -= 1
    return res


print(next_greater_element([4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]))

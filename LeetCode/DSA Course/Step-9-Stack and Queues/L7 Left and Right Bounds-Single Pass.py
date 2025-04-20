from typing import List


def greater_bounds(nums: List[int]):
    n = len(nums)
    left_bound = [-1] * n
    right_bound = [n] * n
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            index = stack.pop()
            right_bound[index] = i
        if stack:
            left_bound[i] = stack[-1]
        stack.append(i)
    print(nums)
    print([i for i in range(n)])
    print(left_bound)
    print(right_bound)


def smaller_bounds(nums: List[int]):
    n = len(nums)
    left_bound = [-1] * n
    right_bound = [n] * n
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] > num:
            index = stack.pop()
            right_bound[index] = i
        if stack:
            left_bound[i] = stack[-1]
        stack.append(i)
    print(nums)
    print([i for i in range(n)])
    print(left_bound)
    print(right_bound)


greater_bounds([1, 7, 3, 5, 7, 8, 9, 2])
smaller_bounds([1, 7, 3, 5, 7, 8, 9, 2])

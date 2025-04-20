def previous_smaller_element(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(n):
        while stack and stack[-1] >= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])

    return res


print(previous_smaller_element([5, 7, 9, 6, 7, 4, 5, 1, 3, 7]))

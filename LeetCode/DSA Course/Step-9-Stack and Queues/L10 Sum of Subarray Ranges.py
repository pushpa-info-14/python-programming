from typing import List


def subarray_ranges(nums: List[int]):
    res = 0
    n = len(nums)
    for i in range(n):
        smallest = nums[i]
        largest = nums[i]
        for j in range(i + 1, n):
            smallest = min(smallest, nums[j])
            largest = max(largest, nums[j])
            res += largest - smallest
    return res


def find_next_smaller_element(arr):
    n = len(arr)
    nse = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            nse[i] = stack[-1]
        stack.append(i)
    return nse


def find_next_larger_element(arr):
    n = len(arr)
    nle = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            nle[i] = stack[-1]
        stack.append(i)
    return nle


def find_previous_smaller_or_equal_element(arr):
    n = len(arr)
    pse = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            pse[i] = stack[-1]
        stack.append(i)
    return pse


def find_previous_larger_or_equal_element(arr):
    n = len(arr)
    ple = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        if stack:
            ple[i] = stack[-1]
        stack.append(i)
    return ple


def sum_subarray_minimum(arr: List[int]) -> int:
    n = len(arr)
    mod = int(1e9 + 7)
    nse = find_next_smaller_element(arr)
    pse = find_previous_smaller_or_equal_element(arr)
    res = 0
    for i in range(n):
        left = i - pse[i]
        right = nse[i] - i
        res = (res + left * right * arr[i]) % mod
    return res


def sum_subarray_maximum(arr: List[int]) -> int:
    n = len(arr)
    mod = int(1e9 + 7)
    nle = find_next_larger_element(arr)
    ple = find_previous_larger_or_equal_element(arr)
    res = 0
    for i in range(n):
        left = i - ple[i]
        right = nle[i] - i
        res = (res + left * right * arr[i]) % mod
    return res


def subarray_ranges2(nums: List[int]):
    return sum_subarray_maximum(nums) - sum_subarray_minimum(nums)


print(subarray_ranges([1, 4, 3, 2]))
print(subarray_ranges2([1, 4, 3, 2]))

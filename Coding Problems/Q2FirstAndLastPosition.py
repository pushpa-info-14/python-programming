"""
Given a sorted array of integers arr and an integer
target, find the index of the first and last position
of target in arr. In target can't be found in
arr, return [-1,-1]
"""


def first_and_last1(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i + 1 < len(arr) and arr[i + 1] == target:
                i += 1
            return [start, i]
    return [-1, -1]


# T(n) = O(n)
# S(n) = O(1)


def find_start(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_end(arr, target):
    if arr[-1] == target:
        return len(arr) - 1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def first_and_last2(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]


# T(n) = 2 * O(logn) = O(logn)
# S(n) = O(1)

arr1 = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
target1 = 5

print(first_and_last1(arr1, target1))
print(first_and_last2(arr1, target1))

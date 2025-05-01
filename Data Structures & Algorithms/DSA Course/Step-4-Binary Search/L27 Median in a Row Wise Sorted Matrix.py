from typing import List


def upperBound(nums: List[int], target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) >> 1
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low


def smallerOrEquals(matrix: List[List[int]], target):
    count = 0
    for i in range(len(matrix)):
        count += upperBound(matrix[i], target)
    return count


def findMedian(matrix: List[List[int]]):
    m = len(matrix)
    n = len(matrix[0])
    low = 0
    high = 0
    for i in range(m):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][n - 1])
    req = m * n // 2
    while low <= high:
        mid = (low + high) >> 1
        smaller_or_equals = smallerOrEquals(matrix, mid)
        if smaller_or_equals <= req:
            low = mid + 1
        else:
            high = mid - 1
    return low


print(findMedian([[1, 5, 7, 9, 11], [2, 3, 4, 5, 10], [9, 10, 12, 14, 16]]))
print(findMedian([[1, 5, 7, 9, 11],
                  [2, 3, 4, 8, 9],
                  [4, 11, 14, 19, 20],
                  [6, 10, 22, 99, 100],
                  [7, 15, 17, 24, 28]]))

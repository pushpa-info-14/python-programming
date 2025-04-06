from typing import List


def binarySearch(nums, target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) >> 1
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == target:
                    return True
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)

        for r in range(m):
            if matrix[r][0] <= target <= matrix[r][-1]:
                return binarySearch(matrix[r], target)
        return False

    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) >> 1
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


s = Solution()
print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))

print(s.searchMatrix2(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
print(s.searchMatrix2(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))

print(s.searchMatrix3(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
print(s.searchMatrix3(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))

from typing import List


def findMax(nums):
    max_index = -1
    max_value = -1
    for i in range(len(nums)):
        if max_value < nums[i]:
            max_index = i
            max_value = nums[i]
    return max_index


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) >> 1
            col = findMax(mat[mid])
            top = mat[mid - 1][col] if mid - 1 >= 0 else -1
            bottom = mat[mid + 1][col] if mid + 1 < m else -1
            element = mat[mid][col]
            if top < element and bottom < element:
                return [mid, col]
            elif element < bottom:
                low = mid + 1
            else:
                high = mid - 1

        return [-1, -1]


s = Solution()
print(s.findPeakGrid(mat=[[1, 4], [3, 2]]))
print(s.findPeakGrid(mat=[[10, 20, 15], [21, 30, 14], [7, 16, 32]]))

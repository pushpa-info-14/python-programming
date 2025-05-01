from typing import List


class Solution:
    def lowerBound(self, nums: List[int], target):
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        max_index = -1
        max_count = 0
        for r in range(m):
            count = n - self.lowerBound(mat[r], 1)
            if max_count < count:
                max_count = count
                max_index = r
        return [max_index, max_count]


# Sorted
s = Solution()
print(s.rowAndMaximumOnes([[0, 1], [1, 1]]))
print(s.rowAndMaximumOnes([[0, 0, 0], [0, 1, 1]]))
print(s.rowAndMaximumOnes([[0, 0], [1, 1], [0, 0]]))
print(s.rowAndMaximumOnes([[0, 0, 1, 1, 1], [0, 0, 0, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 1, 1, 1, 1]]))

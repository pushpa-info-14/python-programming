from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        arr = []
        for row in matrix:
            arr.extend(row)
        arr.sort()
        n = len(arr)

        for i in range(1, n, 2):
            if arr[i - 1] * -1 + arr[i] * -1 > arr[i - 1] + arr[i]:
                arr[i - 1] *= -1
                arr[i] *= -1
        return sum(arr)


s = Solution()
print(s.maxMatrixSum(matrix=[[1, -1], [-1, 1]]))
print(s.maxMatrixSum(matrix=[[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))

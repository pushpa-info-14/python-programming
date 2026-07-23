import math
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row_min = [math.inf] * m
        col_max = [-math.inf] * n

        for r in range(m):
            for c in range(n):
                row_min[r] = min(row_min[r], matrix[r][c])
                col_max[c] = max(col_max[c], matrix[r][c])

        res = []
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == row_min[r] and matrix[r][c] == col_max[c]:
                    res.append(matrix[r][c])
        return res


s = Solution()
print(s.luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(s.luckyNumbers(matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(s.luckyNumbers(matrix=[[7, 8], [1, 2]]))

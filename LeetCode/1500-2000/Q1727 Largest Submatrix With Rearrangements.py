from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        for r in range(m):
            for c in range(n):
                if r > 0 and matrix[r][c] != 0:
                    matrix[r][c] += matrix[r - 1][c]
            cur_row = sorted(matrix[r], reverse=True)
            for i in range(n):
                res = max(res, cur_row[i] * (i + 1))
        return res


s = Solution()
print(s.largestSubmatrix(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
print(s.largestSubmatrix(matrix=[[1, 0, 1, 0, 1]]))
print(s.largestSubmatrix(matrix=[[1, 1, 0], [1, 0, 1]]))

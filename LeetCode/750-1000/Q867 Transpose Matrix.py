from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res = [[0] * m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][r] = matrix[r][c]
        return res


s = Solution()
print(s.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.transpose(matrix=[[1, 2, 3], [4, 5, 6]]))

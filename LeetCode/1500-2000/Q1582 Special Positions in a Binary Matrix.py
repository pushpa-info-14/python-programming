from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        sum_row = [0] * m
        sum_col = [0] * n
        for i in range(m):
            for j in range(n):
                sum_row[i] += mat[i][j]
                sum_col[j] += mat[i][j]
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and sum_row[i] == 1 and sum_col[j] == 1:
                    res += 1
        return res


s = Solution()
print(s.numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
print(s.numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

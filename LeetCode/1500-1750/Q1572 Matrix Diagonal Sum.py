from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            if i != n - i - 1:
                res += mat[i][i] + mat[n - i - 1][i]
            else:
                res += mat[i][i]
        return res


s = Solution()
print(s.diagonalSum(mat=[[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]]))
print(s.diagonalSum(mat=[[1, 1, 1, 1],
                         [1, 1, 1, 1],
                         [1, 1, 1, 1],
                         [1, 1, 1, 1]]))
print(s.diagonalSum(mat=[[5]]))

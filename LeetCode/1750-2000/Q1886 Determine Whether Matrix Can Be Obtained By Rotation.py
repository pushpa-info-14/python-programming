from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate():
            for i in range(n // 2):
                for j in range(n):
                    mat[i][j], mat[n - 1 - i][j] = mat[n - 1 - i][j], mat[i][j]
            for i in range(n):
                for j in range(i + 1):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            return mat == target

        for _ in range(4):
            if rotate():
                return True
        return False


s = Solution()
print(s.findRotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]))
print(s.findRotation(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]))
print(s.findRotation(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]]))

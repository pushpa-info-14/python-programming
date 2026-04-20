class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        res = [0] * n
        for i in range(n):
            for j in range(i, n):
                if matrix[i][j]:
                    res[i] += 1
                    res[j] += 1
        return res

    def findDegrees2(self, matrix: list[list[int]]) -> list[int]:
        return [sum(row) for row in matrix]


s = Solution()
print(s.findDegrees(matrix=[[0, 1, 1], [1, 0, 1], [1, 1, 0]]))
print(s.findDegrees(matrix=[[0, 1, 0], [1, 0, 0], [0, 0, 0]]))
print(s.findDegrees(matrix=[[0]]))
print("-----------")
print(s.findDegrees2(matrix=[[0, 1, 1], [1, 0, 1], [1, 1, 0]]))
print(s.findDegrees2(matrix=[[0, 1, 0], [1, 0, 0], [0, 0, 0]]))
print(s.findDegrees2(matrix=[[0]]))

class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for i1 in range(m):
                        if matrix[i1][j]:
                            matrix[i1][j] = -1
                    for j1 in range(n):
                        if matrix[i][j1]:
                            matrix[i][j1] = -1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

        return matrix

    def setZeroes2(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        row = [1] * m
        col = [1] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0

        for i in range(m):
            for j in range(n):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0

        return matrix

    def setZeroes3(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        col0 = 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # Mark column
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
                    # Mark row
                    matrix[i][0] = 0

        # Process all except first column and row
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Process first column
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # Process first row
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0

        return matrix


s = Solution()
print(s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(s.setZeroes([[1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]))
print(s.setZeroes2([[1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]))
print(s.setZeroes3([[1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]))

print(s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
print(s.setZeroes2([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
print(s.setZeroes3([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))

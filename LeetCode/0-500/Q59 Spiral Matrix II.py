from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        number = 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                matrix[top][i] = number
                number += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = number
                number += 1
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = number
                    number += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = number
                    number += 1
                left += 1

        return matrix


s = Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(1))

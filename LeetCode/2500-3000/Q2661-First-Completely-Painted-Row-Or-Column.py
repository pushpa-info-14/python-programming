from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row = [0 for i in range(m)]
        column = [0 for i in range(n)]

        map = {}
        for i in range(m):
            for j in range(n):
                map[mat[i][j]] = (i, j)

        for i in range(len(arr)):
            x, y = map[arr[i]]
            row[x] += 1
            column[y] += 1

            if row[x] == n or column[y] == m:
                return i


s = Solution()
print(s.firstCompleteIndex([1, 3, 4, 2], [[1, 4], [2, 3]]))
print(s.firstCompleteIndex([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]))
print(s.firstCompleteIndex([1, 4, 5, 2, 6, 3], [[4, 3, 5], [1, 2, 6]]))

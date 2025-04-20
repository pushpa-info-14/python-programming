from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        max_index = -1
        max_count = -1
        for r in range(m):
            count = 0
            for c in range(n):
                count += mat[r][c]
            if max_count < count:
                max_count = count
                max_index = r
        return [max_index, max_count]


s = Solution()
print(s.rowAndMaximumOnes([[0, 1], [1, 0]]))
print(s.rowAndMaximumOnes([[0, 0, 0], [0, 1, 1]]))
print(s.rowAndMaximumOnes([[0, 0], [1, 1], [0, 0]]))

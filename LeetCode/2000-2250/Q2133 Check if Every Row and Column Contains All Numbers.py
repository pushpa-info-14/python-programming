from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for r in range(n):
            seen = set(matrix[r])
            if len(seen) != n:
                return False
        for c in range(n):
            seen = set()
            for r in range(n):
                seen.add(matrix[r][c])
            if len(seen) != n:
                return False
        return True


s = Solution()
print(s.checkValid(matrix=[[1, 2, 3], [3, 1, 2], [2, 3, 1]]))
print(s.checkValid(matrix=[[1, 1, 1], [1, 2, 3], [1, 2, 3]]))

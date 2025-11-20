from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        res = 0
        for r in range(m):
            for c in range(n):
                if (rows[r] + cols[c]) & 1:
                    res += 1
        return res


s = Solution()
print(s.oddCells(m=2, n=3, indices=[[0, 1], [1, 1]]))
print(s.oddCells(m=2, n=2, indices=[[1, 1], [0, 0]]))

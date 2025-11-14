from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        diff_matrix = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff_matrix[r1][c1] += 1
            diff_matrix[r1][c2 + 1] -= 1
            diff_matrix[r2 + 1][c1] -= 1
            diff_matrix[r2 + 1][c2 + 1] += 1

        for r in range(n):
            for c in range(n):
                top = 0 if r == 0 else res[r - 1][c]
                left = 0 if c == 0 else res[r][c - 1]
                top_left = 0 if r == 0 or c == 0 else res[r - 1][c - 1]
                res[r][c] = diff_matrix[r][c] + top + left - top_left

        return res


s = Solution()
print(s.rangeAddQueries(n=3, queries=[[1, 1, 2, 2], [0, 0, 1, 1]]))
print(s.rangeAddQueries(n=2, queries=[[0, 0, 1, 1]]))

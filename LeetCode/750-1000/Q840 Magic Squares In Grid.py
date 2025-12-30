from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0
        res = 0
        for i in range(m - 2):
            for j in range(n - 2):
                row_sum = [0, 0, 0]
                col_sum = [0, 0, 0]
                diagonal1 = 0
                diagonal2 = 0
                seen = set()
                for k in range(3):
                    for l in range(3):
                        val = grid[i + k][j + l]
                        if val < 1 or val > 9 or val in seen:
                            break
                        seen.add(val)
                        if k == l:
                            diagonal1 += val
                        if k + l == 2:
                            diagonal2 += val
                        row_sum[k] += val
                        col_sum[l] += val
                values = set(row_sum + col_sum + [diagonal1, diagonal2])
                if len(values) == 1 and len(seen) == 9:
                    res += 1
        return res


s = Solution()
print(s.numMagicSquaresInside(grid=[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
print(s.numMagicSquaresInside(grid=[[8]]))
print(s.numMagicSquaresInside(grid=[[5, 5, 5], [5, 5, 5], [5, 5, 5]]))

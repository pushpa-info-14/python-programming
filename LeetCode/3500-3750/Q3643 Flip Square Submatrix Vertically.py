from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        top = x
        bottom = x + k - 1
        while top < bottom:
            for c in range(y, y + k):
                temp_top = grid[top][c]
                grid[top][c] = grid[bottom][c]
                grid[bottom][c] = temp_top
            top += 1
            bottom -= 1
        return grid


s = Solution()
print(s.reverseSubmatrix(grid=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], x=1, y=0, k=3))
print(s.reverseSubmatrix(grid=[[3, 4, 2, 3], [2, 3, 4, 2]], x=0, y=2, k=2))

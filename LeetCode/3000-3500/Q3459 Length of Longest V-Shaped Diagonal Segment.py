from functools import cache
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        @cache
        def solver(x, y, dir_idx, can_turn):
            dx, dy = dirs[dir_idx]
            nx, ny = x + dx, y + dy
            target = 2 if grid[x][y] in (0, 1) else 0

            if nx < 0 or nx == m or ny < 0 or ny == n or grid[nx][ny] != target:
                return 0

            no_turn = solver(nx, ny, dir_idx, can_turn)
            turn = 0
            if can_turn:
                turn = solver(nx, ny, (dir_idx + 1) % 4, False)
            return max(no_turn, turn) + 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue

                for d in range(4):
                    ans = max(ans, solver(i, j, d, True) + 1)
        return ans


s = Solution()
print(s.lenOfVDiagonal(grid=[[2, 2, 1, 2, 2], [2, 0, 2, 2, 0], [2, 0, 1, 1, 0], [1, 0, 2, 2, 2], [2, 0, 0, 2, 2]]))  # 5
print(s.lenOfVDiagonal(grid=[[2, 2, 2, 2, 2], [2, 0, 2, 2, 0], [2, 0, 1, 1, 0], [1, 0, 2, 2, 2], [2, 0, 0, 2, 2]]))  # 4
print(s.lenOfVDiagonal(grid=[[1, 2, 2, 2, 2], [2, 2, 2, 2, 0], [2, 0, 0, 0, 0], [0, 0, 2, 2, 2], [2, 0, 0, 2, 0]]))  # 5
print(s.lenOfVDiagonal(grid=[[1]]))  # 1

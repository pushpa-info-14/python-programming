from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[''] * n for _ in range(m)]

        for x, y in guards:
            grid[x][y] = 'G'
        for x, y in walls:
            grid[x][y] = 'W'

        def mark_cells(x, y, dx, dy):
            x += dx
            y += dy
            while 0 <= x < m and 0 <= y < n:
                if grid[x][y] == 'G' or grid[x][y] == 'W':
                    break
                grid[x][y] = '1'
                x += dx
                y += dy

        for x, y in guards:
            mark_cells(x, y, 0, 1)
            mark_cells(x, y, 0, -1)
            mark_cells(x, y, 1, 0)
            mark_cells(x, y, -1, 0)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '':
                    res += 1
        return res


s = Solution()
print(s.countUnguarded(m=4, n=6, guards=[[0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]))
print(s.countUnguarded(m=3, n=3, guards=[[1, 1]], walls=[[0, 1], [1, 0], [2, 1], [1, 2]]))

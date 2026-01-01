from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0] * col for _ in range(row)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def can_cross():
            q = []
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
            visited = [[False] * col for _ in range(row)]
            while q:
                r, c = q.pop()
                if r == row - 1:
                    return True
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0 or nr == row or nc == col or grid[nr][nc] == 1 or visited[nr][nc]:
                        continue
                    q.append((nr, nc))
                    visited[nr][nc] = True
            return False

        low, high = 0, len(cells) - 1
        while low <= high:
            mid = (low + high) // 2
            grid = [[0] * col for _ in range(row)]
            for i in range(mid):
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1

            if can_cross():
                low = mid + 1
            else:
                high = mid - 1
        return high


s = Solution()
print(s.latestDayToCross(row=2, col=2, cells=[[1, 1], [2, 1], [1, 2], [2, 2]]))
print(s.latestDayToCross(row=2, col=2, cells=[[1, 1], [1, 2], [2, 1], [2, 2]]))
print(s.latestDayToCross(row=3, col=3, cells=[[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]))
print(s.latestDayToCross(row=6, col=2,
                         cells=[[4, 2], [6, 2], [2, 1], [4, 1], [6, 1], [3, 1], [2, 2], [3, 2], [1, 1], [5, 1], [5, 2],
                                [1, 2]]))
print(s.latestDayToCross(row=2, col=6,
                         cells=[[1, 4], [1, 3], [2, 1], [2, 5], [2, 2], [1, 5], [2, 4], [1, 2], [1, 6], [2, 3], [2, 6],
                                [1, 1]]))

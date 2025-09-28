from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()

        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        t = 0
        while q and fresh_count > 0:
            q_size = len(q)
            for _ in range(q_size):
                x, y = q.popleft()
                for i in range(4):
                    new_x = x + directions[i][0]
                    new_y = y + directions[i][1]

                    if new_x < 0 or new_y < 0 or new_x == m or new_y == n or (new_x, new_y) in visited:
                        continue
                    if grid[new_x][new_y] != 0:
                        grid[new_x][new_y] = 2
                        fresh_count -= 1
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))
            t += 1

        return t if fresh_count == 0 else -1


s = Solution()
print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(s.orangesRotting([[0, 2]]))
print(s.orangesRotting([[0]]))
print(s.orangesRotting([[1]]))

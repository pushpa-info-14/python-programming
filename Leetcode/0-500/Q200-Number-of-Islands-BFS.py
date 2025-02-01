from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        directions = [-1, 0, 1, 0, -1]

        q = deque()
        island_count = 0

        def bfs(r, c):
            q.append([r, c])
            visited[r][c] = True

            while q:
                x, y = q.popleft()

                for i in range(4):
                    new_x = x + directions[i]
                    new_y = y + directions[i + 1]

                    if new_x < 0 or new_y < 0 or new_x == m or new_y == n or grid[new_x][new_y] == "0" or \
                            visited[new_x][new_y]:
                        continue
                    q.append([new_x, new_y])
                    visited[new_x][new_y] = True

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and not visited[r][c]:
                    bfs(r, c)
                    island_count += 1

        return island_count


s = Solution()
print(s.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))

from collections import deque
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False] * n for _ in range(m)]
        q = deque()

        max_fish = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    q.append((grid[r][c], r, c))
                    visited[r][c] = True

                curr_fish = 0
                while q:
                    fish, x, y = q.popleft()
                    curr_fish += fish
                    max_fish = max(max_fish, curr_fish)

                    for i in range(4):
                        newX = x + directions[i][0]
                        newY = y + directions[i][1]

                        if newX < 0 or newX == m or newY < 0 or newY == n or grid[newX][newY] == 0 or visited[newX][
                            newY]:
                            continue
                        q.append((grid[newX][newY], newX, newY))
                        visited[newX][newY] = True
        return max_fish

    def findMaxFish2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            res = grid[r][c]
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                res += dfs(nr, nc)
            return res

        visited = set()
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (r, c) not in visited:
                    res = max(res, dfs(r, c))
        return res


s = Solution()
print(s.findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
print(s.findMaxFish([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))
print(s.findMaxFish([[6, 1, 10]]))
print(s.findMaxFish2([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
print(s.findMaxFish2([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))
print(s.findMaxFish2([[6, 1, 10]]))

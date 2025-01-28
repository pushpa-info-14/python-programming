from collections import deque
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        q = deque()

        # Mark all land cells as visited
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited.add((i, j))

        max_fish = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    q.append((grid[r][c], r, c))
                    visited.add((r, c))

                curr_fish = 0
                while q:
                    fish, x, y = q.popleft()
                    curr_fish += fish
                    max_fish = max(max_fish, curr_fish)

                    for i in range(4):
                        newX = x + directions[i][0]
                        newY = y + directions[i][1]

                        if newX < 0 or newX == m or newY < 0 or newY == n or (newX, newY) in visited:
                            continue
                        q.append((grid[newX][newY], newX, newY))
                        visited.add((newX, newY))
        return max_fish


s = Solution()
print(s.findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))
print(s.findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))
print(s.findMaxFish([[6,1,10]]))

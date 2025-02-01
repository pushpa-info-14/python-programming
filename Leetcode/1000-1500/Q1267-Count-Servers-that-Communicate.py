from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = [0 for i in range(m)]
        col = [0 for i in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    col[j] += 1
                    row[i] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row[i] > 1 or col[j] > 1):
                    count += 1
        return count


s = Solution()
print(s.countServers([[1, 0], [0, 1]]))
print(s.countServers([[1, 0], [1, 1]]))
print(s.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))

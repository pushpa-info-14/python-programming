from collections import defaultdict
from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        mp = defaultdict(list)

        for r in range(n):
            for c in range(n):
                mp[r - c].append(grid[r][c])
        for key in mp.keys():
            if key >= 0:
                mp[key] = sorted(mp[key])
            else:
                mp[key] = sorted(mp[key], reverse=True)
        for r in range(n):
            for c in range(n):
                grid[r][c] = mp[r - c].pop()

        return grid

s = Solution()
print(s.sortMatrix(grid = [[1,7,3],[9,8,2],[4,5,6]]))
print(s.sortMatrix(grid = [[0,1],[1,2]]))
print(s.sortMatrix(grid = [[1]]))
from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        stronger = [True] * n
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    stronger[j] = False
        res = 0
        for i in range(n):
            if stronger[i]:
                res = i
                break
        return res

    def findChampion2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            if sum(grid[i]) == n - 1:
                return i
        return -1


s = Solution()
print(s.findChampion(grid=[[0, 1], [0, 0]]))
print(s.findChampion(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]]))
print("--------------")
print(s.findChampion2(grid=[[0, 1], [0, 0]]))
print(s.findChampion2(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]]))

from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        sums = set()

        for r in range(m):
            for c in range(n):
                sums.add(grid[r][c])
                size = 1
                while r - size * 2 >= 0 and c - size >= 0 and c + size < n:
                    acc = grid[r][c]
                    acc += grid[r - size * 2][c]
                    acc += grid[r - size][c - size]
                    acc += grid[r - size][c + size]
                    for step in range(1, size):
                        acc += grid[r - step][c - step]
                        acc += grid[r - step][c + step]
                        acc += grid[r - size * 2 + step][c - step]
                        acc += grid[r - size * 2 + step][c + step]
                    sums.add(acc)
                    size += 1
        print(sums)

        return sorted(list(sums), reverse=True)[:3]


s = Solution()
print(
    s.getBiggestThree(grid=[[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]))
print(s.getBiggestThree(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.getBiggestThree(grid=[[7, 7, 7]]))
print(s.getBiggestThree(
    grid=[[20, 17, 9, 13, 5, 2, 9, 1, 5], [14, 9, 9, 9, 16, 18, 3, 4, 12], [18, 15, 10, 20, 19, 20, 15, 12, 11],
          [19, 16, 19, 18, 8, 13, 15, 14, 11], [4, 19, 5, 2, 19, 17, 7, 2, 2]]))

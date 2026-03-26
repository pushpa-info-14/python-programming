from collections import defaultdict
from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total = 0
        counter = defaultdict(int)
        for r in range(m):
            for c in range(n):
                total += grid[r][c]
                counter[grid[r][c]] += 1
        cur = 0
        t_counter = defaultdict(int)
        b_counter = counter.copy()
        for r in range(m - 1):
            for c in range(n):
                cur += grid[r][c]
                t_counter[grid[r][c]] += 1
                b_counter[grid[r][c]] -= 1
                if b_counter[grid[r][c]] == 0:
                    del b_counter[grid[r][c]]
            diff = total - cur * 2
            if diff == 0:
                return True
            elif diff > 0:
                if n == 1:
                    if diff == grid[r + 1][0] or diff == grid[-1][0]:
                        return True
                elif r == m - 2:
                    if diff == grid[r + 1][0] or diff == grid[r + 1][-1]:
                        return True
                else:
                    if diff in b_counter:
                        return True
            else:
                diff = -diff
                if n == 1:
                    if diff == grid[r][0] or diff == grid[0][0]:
                        return True
                elif r == 0:
                    if diff == grid[r][0] or diff == grid[r][-1]:
                        return True
                else:
                    if diff in t_counter:
                        return True
        cur = 0
        l_counter = defaultdict(int)
        r_counter = counter.copy()
        for c in range(n - 1):
            for r in range(m):
                cur += grid[r][c]
                l_counter[grid[r][c]] += 1
                r_counter[grid[r][c]] -= 1
                if r_counter[grid[r][c]] == 0:
                    del r_counter[grid[r][c]]
            diff = total - cur * 2
            if diff == 0:
                return True
            elif diff > 0:
                if m == 1:
                    if diff == grid[0][c + 1] or diff == grid[0][-1]:
                        return True
                elif c == n - 2:
                    if diff == grid[0][-1] or diff == grid[-1][-1]:
                        return True
                else:
                    if diff in r_counter:
                        return True
            else:
                diff = -diff
                if m == 1:
                    if diff == grid[0][0] or diff == grid[0][c]:
                        return True
                elif c == 0:
                    if diff == grid[0][0] or diff == grid[-1][0]:
                        return True
                else:
                    if diff in l_counter:
                        return True
        return False


s = Solution()
print(s.canPartitionGrid(grid=[[1, 4], [2, 3]]))
print(s.canPartitionGrid(grid=[[1, 2], [3, 4]]))
print(s.canPartitionGrid(grid=[[1, 2, 4], [2, 3, 5]]))
print(s.canPartitionGrid(grid=[[4, 1, 8], [3, 2, 6]]))
print(s.canPartitionGrid(grid=[[10, 5, 4, 5]]))
print(s.canPartitionGrid(grid=[[10], [5], [4], [5]]))
print(s.canPartitionGrid(grid=[[25372], [100000], [100000]]))
print(s.canPartitionGrid(grid=[[100000, 90234, 100000, 100000, 100000]]))

from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for layer in range(min(m, n) // 2):
            nums = []
            for c in range(layer, n - 1 - layer):
                nums.append(grid[layer][c])
            for r in range(layer, m - 1 - layer):
                nums.append(grid[r][n - 1 - layer])
            for c in range(n - 1 - layer, layer, -1):
                nums.append(grid[m - 1 - layer][c])
            for r in range(m - 1 - layer, layer, -1):
                nums.append(grid[r][layer])
            nk = k % len(nums)
            nums = nums[nk:] + nums[:nk]
            i = 0
            for c in range(layer, n - 1 - layer):
                grid[layer][c] = nums[i]
                i += 1
            for r in range(layer, m - 1 - layer):
                grid[r][n - 1 - layer] = nums[i]
                i += 1
            for c in range(n - 1 - layer, layer, -1):
                grid[m - 1 - layer][c] = nums[i]
                i += 1
            for r in range(m - 1 - layer, layer, -1):
                grid[r][layer] = nums[i]
                i += 1
        return grid


s = Solution()
print(s.rotateGrid(grid=[[40, 10], [30, 20]], k=1))
print(s.rotateGrid(grid=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], k=2))

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        expected_sum = n * n * (n * n + 1) // 2
        seen = set()

        cur_sum = 0
        repeated = 0
        for i in range(n):
            for j in range(n):
                cur_sum += grid[i][j]
                if grid[i][j] in seen:
                    repeated = grid[i][j]
                seen.add(grid[i][j])

        missing = expected_sum - (cur_sum - repeated)
        return [repeated, missing]


s = Solution()
print(s.findMissingAndRepeatedValues([[1, 3], [2, 2]]))
print(s.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))

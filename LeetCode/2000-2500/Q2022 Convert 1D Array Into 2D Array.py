from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        grid = [[0] * n for _ in range(m)]
        for i in range(len(original)):
            r, c = i // n, i % n
            grid[r][c] = original[i]
        return grid


s = Solution()
print(s.construct2DArray(original=[1, 2, 3, 4], m=2, n=2))
print(s.construct2DArray(original=[1, 2, 3], m=1, n=3))
print(s.construct2DArray(original=[1, 2], m=1, n=1))

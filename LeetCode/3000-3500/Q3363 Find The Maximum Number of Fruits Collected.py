from functools import cache
from math import inf
from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        res = 0
        for idx in range(n):
            res += fruits[idx][idx]
            fruits[idx][idx] = 0

        @cache
        def solve(i, j, c):
            if not (0 <= i < n and 0 <= j < n): return -inf
            if (i, j) == (n - 1, n - 1): return 0
            ans = fruits[i][j]
            if c:
                if i <= j: return -inf
                return ans + max(solve(i - 1, j + 1, c), solve(i, j + 1, c), solve(i + 1, j + 1, c))
            else:
                if i >= j: return -inf
                return ans + max(solve(i + 1, j - 1, c), solve(i + 1, j, c), solve(i + 1, j + 1, c))

        return res + solve(0, n - 1, 0) + solve(n - 1, 0, 1)


s = Solution()
print(s.maxCollectedFruits(fruits=[[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]]))
print(s.maxCollectedFruits(fruits=[[1, 1], [1, 1]]))
print(s.maxCollectedFruits(fruits=[[11, 15, 18, 7], [8, 15, 5, 19], [15, 20, 4, 10], [15, 3, 10, 5]]))

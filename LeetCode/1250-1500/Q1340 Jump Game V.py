from functools import cache
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @cache
        def dfs(i):
            cur = 1
            for j in range(i - 1, i - d - 1, -1):
                if j < 0:
                    continue
                if arr[i] > arr[j]:
                    cur = max(cur, 1 + dfs(j))
                else:
                    break
            for j in range(i + 1, i + d + 1):
                if j >= n:
                    continue
                if arr[i] > arr[j]:
                    cur = max(cur, 1 + dfs(j))
                else:
                    break
            return cur

        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        return res


s = Solution()
print(s.maxJumps(arr=[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], d=2))
print(s.maxJumps(arr=[3, 3, 3, 3, 3], d=3))
print(s.maxJumps(arr=[7, 6, 5, 4, 3, 2, 1], d=1))
print(s.maxJumps(arr=[6, 1, 7, 1, 6, 1], d=2))

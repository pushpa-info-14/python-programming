from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                res = max(res, i)
                break
        for i in range(n - 1):
            if colors[i] != colors[-1]:
                res = max(res, n - 1 - i)
                break
        return res


s = Solution()
print(s.maxDistance(colors=[1, 1, 1, 6, 1, 1, 1]))
print(s.maxDistance(colors=[1, 8, 3, 8, 3]))
print(s.maxDistance(colors=[0, 1]))

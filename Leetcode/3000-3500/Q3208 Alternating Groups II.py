from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = 0
        l = 0
        for r in range(1, n + k - 1):
            if colors[r % n] == colors[r % n - 1]:
                l = r
            if r - l + 1 == k:
                res += 1
                l += 1
        return res


s = Solution()
print(s.numberOfAlternatingGroups(colors=[0, 1, 0, 1, 0], k=3))
print(s.numberOfAlternatingGroups(colors=[0, 1, 0, 0, 1, 0, 1], k=6))
print(s.numberOfAlternatingGroups(colors=[1, 1, 0, 1], k=4))

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res, i, j = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
            j += 1
        return res


s = Solution()
print(s.findContentChildren([1, 5, 3, 3, 4], [4, 2, 1, 2, 1, 3]))

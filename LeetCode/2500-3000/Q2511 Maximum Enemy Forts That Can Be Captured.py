from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        l = 0
        while l < n and forts[l] == 0:
            l += 1
        count = 0
        res = 0
        for r in range(l + 1, n):
            if forts[r] == 0:
                count += 1
            else:
                if forts[l] == -forts[r]:
                    res = max(res, count)
                count = 0
                l = r
        return res


s = Solution()
print(s.captureForts(forts=[1, 0, 0, -1, 0, 0, 0, 0, 1]))
print(s.captureForts(forts=[0, 0, 1, -1]))

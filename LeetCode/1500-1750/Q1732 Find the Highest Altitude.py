from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        cur = 0
        for x in gain:
            cur += x
            res = max(res, cur)
        return res


s = Solution()
print(s.largestAltitude(gain=[-5, 1, 5, 0, -7]))
print(s.largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]))

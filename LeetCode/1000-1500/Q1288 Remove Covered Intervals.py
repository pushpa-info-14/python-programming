from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        l, r = 0, 0
        for x, y in intervals:
            if l <= x and y <= r:
                continue
            else:
                res += 1
            l, r = x, y
        return res


s = Solution()
print(s.removeCoveredIntervals(intervals=[[1, 4], [3, 6], [2, 8]]))
print(s.removeCoveredIntervals(intervals=[[1, 4], [2, 3]]))

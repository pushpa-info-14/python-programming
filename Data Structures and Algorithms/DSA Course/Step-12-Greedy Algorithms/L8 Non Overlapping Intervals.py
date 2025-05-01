import math
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        cnt = 0
        free_at = -math.inf
        for interval in intervals:
            if interval[0] >= free_at:
                cnt += 1
                free_at = interval[1]
        return len(intervals) - cnt


s = Solution()
print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
print(s.eraseOverlapIntervals([[1, 2], [2, 3]]))

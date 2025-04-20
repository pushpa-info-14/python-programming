from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles]
        y = [(r[1], r[3]) for r in rectangles]
        x.sort()
        y.sort()

        def count_non_overlapping_intervals(intervals):
            count = 0
            prev_end = -1
            for start, end in intervals:
                if prev_end <= start:
                    count += 1
                prev_end = max(prev_end, end)
            return count

        return max(count_non_overlapping_intervals(x), count_non_overlapping_intervals(y)) >= 3


s = Solution()
print(s.checkValidCuts(n=5, rectangles=[[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]))
print(s.checkValidCuts(n=4, rectangles=[[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]))
print(s.checkValidCuts(n=4, rectangles=[[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]))

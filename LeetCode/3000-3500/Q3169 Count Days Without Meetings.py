from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        prev_end = 0
        for start, end in meetings:
            start = max(start, prev_end + 1)
            length = end - start + 1
            days -= max(length, 0)
            prev_end = max(prev_end, end)
        return days


s = Solution()
print(s.countDays(days=10, meetings=[[5, 7], [1, 3], [9, 10]]))
print(s.countDays(days=5, meetings=[[2, 4], [1, 3]]))
print(s.countDays(days=6, meetings=[[1, 6]]))

from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        last = max_prev_gap = best = 0
        for i in range(n):
            start, end = startTime[i], endTime[i]
            next_start = startTime[i + 1] if i + 1 < n else eventTime
            if end - start <= max_prev_gap:
                best = max(best, next_start - last)
            else:
                best = max(best, next_start - last - (end - start))
            max_prev_gap = max(max_prev_gap, start - last)
            last = end

        max_prev_gap = 0
        last = eventTime
        for i in range(n - 1, -1, -1):
            start, end = startTime[i], endTime[i]
            next_end = endTime[i - 1] if i - 1 >= 0 else 0
            if end - start <= max_prev_gap:
                best = max(best, last - next_end)
            max_prev_gap = max(max_prev_gap, last - end)
            last = start
        return best


s = Solution()
print(s.maxFreeTime(eventTime=5, startTime=[1, 3], endTime=[2, 5]))
print(s.maxFreeTime(eventTime=10, startTime=[0, 7, 9], endTime=[1, 8, 10]))
print(s.maxFreeTime(eventTime=10, startTime=[0, 3, 7, 9], endTime=[1, 4, 8, 10]))
print(s.maxFreeTime(eventTime=5, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]))

"""
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend
all meetings.
"""

from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def can_attend(intervals: List[Interval]):
    intervals.sort(key=lambda x: x.start)

    prev_end = intervals[0].end
    for interval in intervals[1:]:
        if prev_end <= interval.start:
            prev_end = interval.end
        else:
            return False
    return True


print(can_attend([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
print(can_attend([Interval(0, 5), Interval(5, 10), Interval(15, 20)]))

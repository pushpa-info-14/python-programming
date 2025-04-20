"""
Given an array of meeting time intervals consisting of start and end times, find the minimum number of
conference rooms required.
"""

from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def number_of_meeting_rooms(intervals: List[Interval]):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res, count = 0, 0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res


def number_of_meeting_rooms2(intervals: List[Interval]):
    intervals.sort(key=lambda x: x.start)

    results = [intervals[0]]
    for interval in intervals[1:]:
        is_required_new = False
        for result in results:
            if result.end <= interval.start:
                result.end = interval.end
                is_required_new = False
            else:
                is_required_new = True
        if is_required_new:
            results.append(interval)
    return len(results)


print(number_of_meeting_rooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
print(number_of_meeting_rooms([Interval(0, 5), Interval(5, 10), Interval(15, 20)]))
print(number_of_meeting_rooms2([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
print(number_of_meeting_rooms2([Interval(0, 5), Interval(5, 10), Interval(15, 20)]))

"""
You are given an array of non-overlapping intervals where
intervals[i] = [starti, endi] represent the start and the end
of the ith interval and intervals is sorted in ascending order
by starti. You are also given an interval newInterval = [start, end]
that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted
in ascending order by starti and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
from typing import List


def insert_interval(intervals: List[List[int]], new_interval: List[int]):
    res = []
    for i in range(len(intervals)):
        if new_interval[1] < intervals[i][0]:
            res.append(new_interval)
            return res + intervals[i:]
        elif new_interval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            min_val = min(new_interval[0], intervals[i][0])
            max_val = max(new_interval[1], intervals[i][1])
            new_interval = [min_val, max_val]

    res.append(new_interval)
    return res


print(insert_interval([[1, 3], [6, 9]], [2, 5]))
print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))

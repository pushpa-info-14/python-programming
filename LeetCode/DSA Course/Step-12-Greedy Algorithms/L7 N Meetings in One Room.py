from typing import List


def maxMeetings(start: List[int], end: List[int]):
    intervals = []
    for i in range(len(start)):
        intervals.append((i, start[i], end[i]))
    intervals.sort(key=lambda x: x[2])

    cnt = 0
    free_at = -1

    for meeting in intervals:
        if meeting[1] > free_at:
            cnt += 1
            free_at = meeting[2]

    return cnt


print(maxMeetings([0, 3, 1, 5, 5, 8], [5, 4, 2, 9, 7, 9]))

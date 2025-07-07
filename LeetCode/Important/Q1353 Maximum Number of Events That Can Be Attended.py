import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        i = 0
        t = 1
        attended = 0
        min_heap = []

        while i < n or min_heap:
            # Time skip: to cover only timeline covered by at least one event
            if not min_heap:
                t = max(t, events[i][0])

            # Add events starting at current index
            while i < n and events[i][0] == t:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # Remove all already ended (unattended) events
            while min_heap and min_heap[0] < t:
                heapq.heappop(min_heap)

            # Pop 1 event at current time
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
            t += 1

        return attended


s = Solution()
print(s.maxEvents(events=[[1, 2], [2, 3], [3, 4]]))
print(s.maxEvents(events=[[1, 2], [2, 3], [3, 4], [1, 2]]))

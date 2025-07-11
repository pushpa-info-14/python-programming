import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counts = [0] * n
        unused = [i for i in range(n)]
        heapq.heapify(unused)
        available = []

        type_start = 1
        type_end = 0
        events = []
        for s, e in meetings:
            events.append((s, type_start, e - s))
        heapq.heapify(events)

        while events:
            t, ty, c = heapq.heappop(events)

            if ty == type_start:
                # We can just put this meeting into available
                duration = c
                heapq.heappush(available, (t, duration))
            else:
                # Free up the room
                current_room = c
                heapq.heappush(unused, current_room)

            while unused and available:
                # t is the current time, let's get a room.
                current_room = heapq.heappop(unused)
                counts[current_room] += 1
                _, duration = heapq.heappop(available)

                heapq.heappush(events, (t + duration, type_end, current_room))

        max_count = 0
        max_index = -1

        for i in reversed(range(n)):
            if max_count <= counts[i]:
                max_count = counts[i]
                max_index = i

        return max_index

    def mostBooked2(self, n: int, meetings: List[List[int]]) -> int:
        available = list(range(n))
        used = []
        counts = [0] * n
        for s, e in sorted(meetings):
            while used and used[0][0] <= s:
                heapq.heappush(available, heapq.heappop(used)[1])
            if available:
                room = heapq.heappop(available)
                heapq.heappush(used, (e, room))
                counts[room] += 1
            else:
                t, room = heapq.heappop(used)
                heapq.heappush(used, (t + e - s, room))
                counts[room] += 1
        return counts.index(max(counts))


solution = Solution()
print(solution.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
print(solution.mostBooked(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
print(solution.mostBooked2(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
print(solution.mostBooked2(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))

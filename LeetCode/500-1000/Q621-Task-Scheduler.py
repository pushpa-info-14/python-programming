import heapq
from collections import deque
from typing import List, Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]

        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time


s = Solution()
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(s.leastInterval(["A", "C", "A", "B", "D", "B"], 1))

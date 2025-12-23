import heapq
from bisect import bisect_left
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        memo = {}

        def dfs(i, count):
            if (i, count) in memo:
                return memo[(i, count)]
            if i == n or count == 0:
                return 0
            not_take = dfs(i + 1, count)
            nxt = bisect_left(events, events[i][1] + 1, key=lambda x: x[0])
            take = events[i][2] + dfs(nxt, count - 1)
            memo[(i, count)] = max(not_take, take)
            return memo[(i, count)]

        return dfs(0, 2)

    def maxTwoEvents2(self, events: List[List[int]]) -> int:
        events.sort()
        q = []
        res = 0
        max_value = 0
        for start, end, value in events:
            while q and q[0][0] < start:
                max_value = max(max_value, q[0][1])
                heapq.heappop(q)
            res = max(res, max_value + value)
            heapq.heappush(q, (end, value))
        return res


s = Solution()
print(s.maxTwoEvents(events=[[1, 3, 2], [4, 5, 2], [2, 4, 3]]))
print(s.maxTwoEvents(events=[[1, 3, 2], [4, 5, 2], [1, 5, 5]]))
print(s.maxTwoEvents(events=[[1, 5, 3], [1, 5, 1], [6, 6, 5]]))
print(s.maxTwoEvents(
    events=[[66, 97, 90], [98, 98, 68], [38, 49, 63], [91, 100, 42], [92, 100, 22], [1, 77, 50], [64, 72, 97]]))
print("--------------")
print(s.maxTwoEvents2(events=[[1, 3, 2], [4, 5, 2], [2, 4, 3]]))
print(s.maxTwoEvents2(events=[[1, 3, 2], [4, 5, 2], [1, 5, 5]]))
print(s.maxTwoEvents2(events=[[1, 5, 3], [1, 5, 1], [6, 6, 5]]))
print(s.maxTwoEvents2(
    events=[[66, 97, 90], [98, 98, 68], [38, 49, 63], [91, 100, 42], [92, 100, 22], [1, 77, 50], [64, 72, 97]]))

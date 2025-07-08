import bisect
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        start_days = [i[0] for i in events]
        next_event = [n] * n
        for i in range(n):
            next_event[i] = bisect.bisect_right(start_days, events[i][1])
        memo = [[-1] * (k + 1) for _ in range(n)]

        def dfs(i, k):
            if k == 0 or i == n:
                return 0

            if memo[i][k] != -1:
                return memo[i][k]

            skip_event = dfs(i + 1, k)
            attend_event = dfs(next_event[i], k - 1) + events[i][2]
            memo[i][k] = max(skip_event, attend_event)
            return memo[i][k]

        return dfs(0, k)


s = Solution()
print(s.maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2))
print(s.maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 10]], k=2))
print(s.maxValue(events=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k=3))

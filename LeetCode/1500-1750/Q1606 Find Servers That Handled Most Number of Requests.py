import bisect
import heapq

from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        n = len(arrival)
        available_servers = SortedList([i for i in range(k)])
        counter = [0] * k
        running_requests = []
        for i in range(n):
            t = arrival[i]
            duration = load[i]
            while running_requests and running_requests[0][0] <= t:
                available_servers.add(heapq.heappop(running_requests)[1])

            if available_servers:
                idx = bisect.bisect_left(available_servers, i % k)
                if idx == len(available_servers):
                    idx = 0
                server = available_servers[idx]
                counter[server] += 1
                heapq.heappush(running_requests, (t + duration, server))
                available_servers.remove(server)
        mx = max(counter)
        res = []
        for i, count in enumerate(counter):
            if count == mx:
                res.append(i)
        return res


s = Solution()
print(s.busiestServers(k=3, arrival=[1, 2, 3, 4, 5], load=[5, 2, 3, 3, 3]))
print(s.busiestServers(k=3, arrival=[1, 2, 3, 4], load=[1, 2, 1, 2]))
print(s.busiestServers(k=3, arrival=[1, 2, 3], load=[10, 12, 11]))

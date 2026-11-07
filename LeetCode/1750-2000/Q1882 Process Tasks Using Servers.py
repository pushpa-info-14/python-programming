import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        running_tasks = []  # (end_time, (weight, i))
        res = []
        t = 0
        for tt, time_needed in enumerate(tasks):
            while running_tasks and running_tasks[0][0] <= t:
                end_time, server_info = heapq.heappop(running_tasks)
                heapq.heappush(free_servers, server_info)
            if not free_servers:
                end_time = running_tasks[0][0]
                while running_tasks and running_tasks[0][0] == end_time:
                    end_time, server_info = heapq.heappop(running_tasks)
                    heapq.heappush(free_servers, server_info)
                t = end_time
            server_info = heapq.heappop(free_servers)
            heapq.heappush(running_tasks, (t + time_needed, server_info))
            res.append(server_info[1])
            t = max(t, tt + 1)

        return res


s = Solution()
print(s.assignTasks(servers=[3, 3, 2], tasks=[1, 2, 3, 2, 1, 2]))
print(s.assignTasks(servers=[5, 1, 4, 3, 2], tasks=[2, 1, 2, 4, 5, 2, 1]))

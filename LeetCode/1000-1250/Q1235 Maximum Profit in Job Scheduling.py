from typing import List


class Job:
    def __init__(self, id, start_time, end_time, profit):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.profit = profit


class Solution:
    def find(self, jobs: List[Job], start, target):
        l, r = start, len(jobs) - 1
        while l <= r:
            m = (l + r) // 2
            if jobs[m].start_time < target:
                l = m + 1
            else:
                r = m - 1
        return l

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = []
        max_deadline = 0

        for i in range(n):
            max_deadline = max(max_deadline, endTime[i])
            jobs.append(Job(i, startTime[i], endTime[i], profit[i]))

        jobs.sort(key=lambda x: x.start_time)

        # for job in jobs:
        #     print(job.id, job.start_time, job.end_time, job.profit)

        # intervals = sorted(zip(startTime, endTime, profit))
        # print(intervals)

        memo = {}

        def dfs(i):
            if i == n:
                return 0

            if i in memo:
                return memo[i]

            # Do not include
            res = dfs(i + 1)

            # Include
            # j = i + 1
            # while j < n:
            #     if jobs[i].end_time <= jobs[j].start_time:
            #         break
            #     j += 1
            j = self.find(jobs, i, jobs[i].end_time)

            res = max(res, jobs[i].profit + dfs(j))
            memo[i] = res
            return res

        return dfs(0)

    def find2(self, jobs, start, target):
        l, r = start, len(jobs) - 1
        while l <= r:
            m = (l + r) // 2
            if jobs[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        return l

    def jobScheduling2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = sorted(zip(startTime, endTime, profit))
        memo = {}

        def dfs(i):
            if i == n:
                return 0

            if i in memo:
                return memo[i]

            # Do not include
            res = dfs(i + 1)

            # Include
            j = self.find2(jobs, i, jobs[i][1])

            res = max(res, jobs[i][2] + dfs(j))
            memo[i] = res
            return res

        return dfs(0)


s = Solution()
print(s.jobScheduling(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]))
print(s.jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]))
print(s.jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]))
print(s.jobScheduling2(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]))
print(s.jobScheduling2(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]))
print(s.jobScheduling2(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]))

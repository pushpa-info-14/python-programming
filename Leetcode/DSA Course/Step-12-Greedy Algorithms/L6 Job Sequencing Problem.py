from typing import List

from Leetcode.Common.Job import Job1


def maxProfit(jobs: List[Job1]):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    # for job in jobs:
    #     print(job.id, job.deadline, job.profit)

    max_deadline = 0
    for job in jobs:
        max_deadline = max(max_deadline, job.deadline)

    schedule = [-1] * (max_deadline + 1)
    profit = 0
    completed = 0
    for job in jobs:
        for i in range(job.deadline, 0, -1):  # Depending on the question day 0 can be possible
            if schedule[i] == -1:
                schedule[i] = job.id
                profit += job.profit
                completed += 1
                break
    return [completed, profit]


inputs = [
    Job1(1, 4, 20),
    Job1(2, 5, 60),
    Job1(3, 6, 70),
    Job1(4, 6, 65),
    Job1(5, 4, 25),
    Job1(6, 2, 80),
    Job1(7, 2, 10),
    Job1(8, 2, 22)
]

print(maxProfit(inputs))

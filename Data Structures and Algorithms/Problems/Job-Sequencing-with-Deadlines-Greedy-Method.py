from typing import List


class Solution:
    def job_sequencing(self, jobs: List[str], profits: List[int], deadlines: List[int]):
        job_count = len(jobs)
        max_slots = 0
        for deadline in deadlines:
            if max_slots < deadline:
                max_slots = deadline
        slot_job = ["" for _ in range(max_slots)]
        slot_profit = [-1 for _ in range(max_slots)]

        for i in range(job_count):
            deadline = deadlines[i]
            slot_index = deadline - 1
            while slot_index >= 0:
                if slot_job[slot_index] == "":
                    slot_job[slot_index] = jobs[i]
                    slot_profit[slot_index] = profits[i]
                    break
                slot_index -= 1

        print(slot_job)
        print(slot_profit)
        return


s = Solution()

jobs = ["J1", "J2", "J3", "J4", "J5", "J6", "J7"]
profits = [35, 30, 25, 20, 15, 12, 5]
deadlines = [3, 4, 4, 2, 3, 1, 2]

print(s.job_sequencing(jobs, profits, deadlines))

from typing import List


def averageWaitingTime(tasks: List[int]):
    tasks.sort()
    t = 0
    wait_time = 0
    for task in tasks:
        wait_time += t
        t += task

    return wait_time // len(tasks)


print(averageWaitingTime([4, 3, 7, 1, 2]))

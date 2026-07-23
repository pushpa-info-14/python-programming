import heapq
from typing import List


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_details = {}
        self.task_queue = []
        for user_id, task_id, priority in tasks:
            self.task_details[task_id] = (priority, user_id)
            heapq.heappush(self.task_queue, (-priority, -task_id, user_id))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_details[taskId] = (priority, userId)
        heapq.heappush(self.task_queue, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        user_id = self.task_details[taskId][1]
        self.task_details[taskId] = (newPriority, user_id)
        heapq.heappush(self.task_queue, (-newPriority, -taskId, user_id))

    def rmv(self, taskId: int) -> None:
        del self.task_details[taskId]

    def execTop(self) -> int:
        while self.task_queue:
            priority, task_id, user_id = heapq.heappop(self.task_queue)
            priority, task_id = -priority, -task_id
            if task_id in self.task_details and self.task_details[task_id] == (priority, user_id):
                del self.task_details[task_id]
                return user_id
        return -1


taskManager = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
taskManager.add(4, 104, 5)
taskManager.edit(102, 8)
print(taskManager.execTop())
taskManager.rmv(101)
taskManager.add(5, 105, 15)
print(taskManager.execTop())

taskManager = TaskManager([[1, 101, 8], [2, 102, 20], [3, 103, 5]])
taskManager.add(4, 104, 5)
taskManager.edit(102, 9)
print(taskManager.execTop())
taskManager.rmv(101)
taskManager.add(50, 101, 8)
print(taskManager.execTop())

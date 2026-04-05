import heapq
from collections import defaultdict


class EventManager:
    def __init__(self, events: list[list[int]]):
        self.mp = defaultdict(int)
        self.q = []
        for eventId, priority in events:
            self.mp[eventId] = priority
            heapq.heappush(self.q, (-priority, eventId))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.mp[eventId] = newPriority
        heapq.heappush(self.q, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.q:
            priority, eventId = heapq.heappop(self.q)
            if self.mp[eventId] == -priority:
                self.mp[eventId] = 0
                return eventId
        return -1


eventManager = EventManager([[5, 7], [2, 7], [9, 4]])
print(eventManager.pollHighest())
eventManager.updatePriority(9, 7)
print(eventManager.pollHighest())
print(eventManager.pollHighest())
print("------------")
eventManager = EventManager([[20, 6], [13, 2], [14, 7], [17, 2]])
eventManager.updatePriority(13, 8)
eventManager.updatePriority(13, 1)
eventManager.updatePriority(13, 8)
print(eventManager.pollHighest())
print(eventManager.pollHighest())
eventManager.updatePriority(20, 5)

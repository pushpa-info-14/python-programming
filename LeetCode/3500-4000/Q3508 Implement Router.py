import bisect
from collections import deque, defaultdict
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        self._set = set()
        self._memory_limit = memoryLimit
        self._buffer = deque()
        self._destinations = defaultdict(deque)

    @staticmethod
    def getKey(source: int, destination: int, timestamp: int):
        return f"{source}-{destination}-{timestamp}"

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self.getKey(source, destination, timestamp)
        if key not in self._set:
            if len(self._buffer) == self._memory_limit:
                self.forwardPacket()
            self._buffer.append([source, destination, timestamp])
            self._set.add(key)
            self._destinations[destination].append(timestamp)
            return True
        return False

    def forwardPacket(self) -> List[int]:
        if self._buffer:
            packet = self._buffer.popleft()
            key = self.getKey(packet[0], packet[1], packet[2])
            self._set.remove(key)
            self._destinations[packet[1]].popleft()
            return packet
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        return bisect.bisect_right(self._destinations[destination], endTime) - bisect.bisect_left(
            self._destinations[destination], startTime)


router = Router(3)
router.addPacket(1, 4, 90)
router.addPacket(2, 5, 90)
router.addPacket(1, 4, 90)
router.addPacket(3, 5, 95)
router.addPacket(4, 5, 105)
print(router.forwardPacket())
router.addPacket(5, 2, 110)
print(router.getCount(5, 100, 110))

router = Router(4)
router.addPacket(4, 5, 1)
print(router.getCount(5, 1, 1))

router = Router(2)
router.addPacket(3, 1, 3)
router.addPacket(1, 2, 3)
router.addPacket(4, 5, 3)
print(router.getCount(1, 2, 3))

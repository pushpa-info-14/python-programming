class RecentCounter:
    def __init__(self):
        self._requests = []

    def ping(self, t: int) -> int:
        self._requests.append(t)
        while self._requests[0] < self._requests[-1] - 3000:
            self._requests.pop(0)
        return len(self._requests)


s = RecentCounter()
print(s.ping(1))
print(s.ping(100))
print(s.ping(3001))
print(s.ping(3002))

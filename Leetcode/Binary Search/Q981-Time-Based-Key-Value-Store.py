class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store.get(key, [])
        n = len(values)
        res = ""
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp >= values[mid][0]:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set("foo", "bar", 1)
# obj.set("foo", "bar", 5)
# obj.set("foo", "bar", 2)
# print(obj.get("foo", 0))
# print(obj.get("foo", 2))
# print(obj.get("foo", 5))

obj = TimeMap()
obj.set("love", "high", 10)
obj.set("love", "low", 20)
print(obj.get("love", 5))
print(obj.get("love", 10))
print(obj.get("love", 15))
print(obj.get("love", 20))
print(obj.get("love", 25))

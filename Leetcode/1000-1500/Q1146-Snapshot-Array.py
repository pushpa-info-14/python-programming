class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot_array = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.snapshot_array[index][-1][0] == self.snap_id:
            self.snapshot_array[index][-1][1] = val
        else:
            self.snapshot_array[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshots = self.snapshot_array[index]

        l, r = 0, len(snapshots) - 1
        while l <= r:
            mid = (l + r) // 2
            if snap_id < snapshots[mid][0]:
                r = mid - 1
            elif snap_id > snapshots[mid][0]:
                l = mid + 1
            else:
                return snapshots[mid][1]
        return snapshots[r][1]


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
# obj.set(0, 5)
# obj.set(0, 59)
# obj.set(0, 7)
# obj.snap() # 0
# obj.set(0, 6)
# obj.snap() # 1
# obj.snap() # 2
# obj.snap() # 3
# obj.set(0, 0)
# obj.snap() # 4
# print(obj.get(0, 0))
# print(obj.get(0, 1))
# print(obj.get(0, 2))
# print(obj.get(0, 3))
# print(obj.get(0, 4))

obj = SnapshotArray(1)
obj.set(0, 4)
obj.set(0, 16)
obj.set(0, 13)
obj.snap()  # 0
print(obj.get(0, 0))

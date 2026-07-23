from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class DisjointSet:
    def __init__(self):
        self._parent = {}

    def findParent(self, x):
        if x not in self._parent:
            self._parent[x] = x
        while x != self._parent[x]:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x

    def union(self, x, y):
        self._parent[self.findParent(x)] = self._parent[self.findParent(y)]

    def groups(self):
        groups = defaultdict(set)
        for x in self._parent:
            groups[self.findParent(x)].add(x)
        return groups.values()


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        seen = {0, firstPerson}
        mp = defaultdict(list)
        for x, y, t in meetings:
            mp[t].append([x, y])
        for t in sorted(mp.keys()):
            pairs = mp[t]
            while True:
                temp = []
                for x, y in pairs:
                    if x in seen:
                        seen.add(y)
                    elif y in seen:
                        seen.add(x)
                    else:
                        temp.append([x, y])
                if len(temp) == len(pairs):
                    break
                pairs = temp
        return list(seen)

    def findAllPeople2(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = {0, firstPerson}
        mp = defaultdict(list)
        for x, y, t in meetings:
            mp[t].append([x, y])
        for t in sorted(mp.keys()):
            ds = DisjointSet()
            for x, y in mp[t]:
                ds.union(x, y)
            for group in ds.groups():
                for x in group:
                    if x in known:
                        known |= group
                        break
        return list(known)

    def findAllPeople3(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = defaultdict(list)
        for x, y, t in [[0, firstPerson, 0]] + meetings:
            adj[x].append((t, y))
            adj[y].append((t, x))
        res = {0}
        q = [(0, 0, firstPerson)]
        while q:
            t, x, y = heappop(q)
            for dt, dy in adj[y]:
                if dt >= t:
                    heappush(q, (dt, y, dy))
            adj[y].clear()
            res.add(y)
        return list(res)


s = Solution()
print(s.findAllPeople(n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1))
print(s.findAllPeople(n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3))
print(s.findAllPeople(n=5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1))
print(s.findAllPeople(n=5, meetings=[[1, 4, 3], [0, 4, 3]], firstPerson=3))
print("----------------------------")
print(s.findAllPeople2(n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1))
print(s.findAllPeople2(n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3))
print(s.findAllPeople2(n=5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1))
print(s.findAllPeople2(n=5, meetings=[[1, 4, 3], [0, 4, 3]], firstPerson=3))
print("----------------------------")
print(s.findAllPeople3(n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1))
print(s.findAllPeople3(n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3))
print(s.findAllPeople3(n=5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1))
print(s.findAllPeople3(n=5, meetings=[[1, 4, 3], [0, 4, 3]], firstPerson=3))

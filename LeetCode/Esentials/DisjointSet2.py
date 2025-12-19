from collections import defaultdict


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
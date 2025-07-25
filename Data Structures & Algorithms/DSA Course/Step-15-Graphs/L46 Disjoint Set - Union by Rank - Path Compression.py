class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))

    def findParent(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.findParent(x)
        y = self.findParent(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.rank[y] += 1
            else:
                self.parent[y] = x
                self.rank[x] += 1


ds = DisjointSet(7)
ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(5, 6)

if ds.findParent(3) == ds.findParent(7):
    print("same")
else:
    print("not same")

ds.union(3, 7)

if ds.findParent(3) == ds.findParent(7):
    print("same")
else:
    print("not same")

# rank is distorted with path compression. So size will be used.

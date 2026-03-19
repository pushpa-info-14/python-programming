class DisjointSet:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = list(range(n + 1))

    def findParent(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.findParent(x)
        y = self.findParent(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]


class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        x_map = {}
        y_map = {}
        n = len(points)
        ds = DisjointSet(n)
        for i in range(n):
            x = points[i][0]
            y = points[i][1]
            if x in x_map:
                ds.union(i, x_map[x])
            else:
                x_map[x] = i
            if y in y_map:
                ds.union(i, y_map[y])
            else:
                y_map[y] = i
        comp = [0] * n
        for i in range(n):
            comp[ds.findParent(i)] += 1
        comp.sort(reverse=True)

        if len(comp) < 2:
            return n + 1
        return comp[0] + comp[1] + 1


s = Solution()
print(s.maxActivated(points=[[1, 1], [1, 2], [2, 2]]))
print(s.maxActivated(points=[[2, 2], [1, 1], [3, 3]]))
print(s.maxActivated(points=[[2, 3], [2, 2], [1, 1], [4, 5]]))

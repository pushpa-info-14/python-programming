class DisjointSet:
    def __init__(self, n):
        self.size = [0] * (n + 1)
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


def numOfIslandsII(n, m, q):
    visited = [[0] * m for _ in range(n)]
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    ds = DisjointSet(n * m)

    res = []
    count = 0
    for r, c in q:
        if visited[r][c]:
            res.append(count)
            continue
        visited[r][c] = 1
        count += 1
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr == n or nc < 0 or nc == m or not visited[nr][nc]:
                continue
            node = r * m + c
            new_node = nr * m + nc
            if ds.findParent(node) != ds.findParent(new_node):
                count -= 1
                ds.union(node, new_node)
        res.append(count)

    return res


print(numOfIslandsII(4, 5,
                     [[0, 0], [0, 0], [1, 1], [1, 0], [0, 1], [0, 3], [1, 3], [0, 4], [3, 2], [2, 2], [1, 2], [0, 2]]))

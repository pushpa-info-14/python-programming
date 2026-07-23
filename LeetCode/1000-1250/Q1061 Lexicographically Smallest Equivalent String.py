from collections import defaultdict


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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        adj_list = defaultdict(list)
        for a, b in zip(s1, s2):
            if a != b:
                adj_list[a].append(b)
                adj_list[b].append(a)

        def group(cur, smallest, mp):
            if cur < smallest:
                smallest = cur
            mp.add(cur)

            for nei in adj_list[cur]:
                if nei not in mp:
                    smallest = group(nei, smallest, mp)
            return smallest

        base = list(baseStr)
        for i, c in enumerate(base):
            char = group(c, c, set())
            base[i] = char

        return "".join(base)

    def smallestEquivalentString2(self, s1: str, s2: str, baseStr: str) -> str:

        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = x
            if uf[x] == x:
                return x
            uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            p1 = find(x)
            p2 = find(y)
            if p1 == p2:
                return
            if p1 > p2:
                uf[p1] = p2
            else:
                uf[p2] = p1

        for i in range(len(s1)):
            union(s1[i], s2[i])

        ans = []
        for j in range(len(baseStr)):
            ans.append(find(baseStr[j]))

        return "".join(ans)


s = Solution()
print(s.smallestEquivalentString(s1="parker", s2="morris", baseStr="parser"))
print(s.smallestEquivalentString(s1="hello", s2="world", baseStr="hold"))
print(s.smallestEquivalentString(s1="leetcode", s2="programs", baseStr="sourcecode"))
print(s.smallestEquivalentString2(s1="parker", s2="morris", baseStr="parser"))
print(s.smallestEquivalentString2(s1="hello", s2="world", baseStr="hold"))
print(s.smallestEquivalentString2(s1="leetcode", s2="programs", baseStr="sourcecode"))

from collections import defaultdict
from typing import List


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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)
        index_by_email = {}

        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in index_by_email:
                    ds.union(i, index_by_email[email])
                else:
                    index_by_email[email] = i

        mp = defaultdict(list)
        for email in index_by_email.keys():
            parent = ds.findParent(index_by_email[email])
            mp[parent].append(email)

        res = []
        for idx in mp.keys():
            mp[idx].sort()
            res.append([accounts[idx][0]] + mp[idx])

        return res


# LeetCode 721
s = Solution()
print(s.accountsMerge(accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                                ["John", "johnsmith@mail.com", "john00@mail.com"],
                                ["Mary", "mary@mail.com"],
                                ["John", "johnnybravo@mail.com"]]))
print(s.accountsMerge(accounts=[["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                                ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                                ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                                ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                                ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]))

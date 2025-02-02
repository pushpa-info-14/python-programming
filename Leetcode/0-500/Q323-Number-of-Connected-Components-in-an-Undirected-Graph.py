from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return x

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


s = Solution()
print(s.countComponents(5, [[0, 1], [1, 2], [3, 4]]))

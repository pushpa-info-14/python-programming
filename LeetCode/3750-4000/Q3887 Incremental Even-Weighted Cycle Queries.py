from typing import List


class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        xor = [0] * n

        def find(x):
            if x != parent[x]:
                root = find(parent[x])
                xor[x] ^= xor[parent[x]]
                parent[x] = root
            return parent[x]

        res = 0
        for u, v, w in edges:
            p1 = find(u)
            p2 = find(v)
            if p1 == p2:
                if xor[u] ^ xor[v] ^ w == 0:
                    res += 1
            else:
                parent[p1] = p2
                xor[p1] = xor[u] ^ xor[v] ^ w
                res += 1

        return res


s = Solution()
print(s.numberOfEdgesAdded(n=3, edges=[[0, 1, 1], [1, 2, 1], [0, 2, 1]]))
print(s.numberOfEdgesAdded(n=3, edges=[[0, 1, 1], [1, 2, 1], [0, 2, 0]]))

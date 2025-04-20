from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(_v, components):
            if _v in visited:
                return
            visited.add(_v)
            components.append(_v)
            for nei in adj[_v]:
                dfs(nei, components)
            return components

        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        res = 0
        visited = set()
        for v in range(n):
            if v in visited:
                continue
            component = dfs(v, [])
            if all([len(component) - 1 == len(adj[v2]) for v2 in component]):
                res += 1
            # flag = True
            # for v2 in component:
            #     if len(component) - 1 != len(adj[v2]):
            #         flag = False
            #         break
            # if flag:
            #     res += 1
        return res


s = Solution()
print(s.countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]]))
print(s.countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))

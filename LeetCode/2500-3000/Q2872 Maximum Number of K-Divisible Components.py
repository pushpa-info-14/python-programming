from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        components = 1

        def dfs(parent, node):
            nonlocal components
            parent_sum = values[node]
            for nei in adj[node]:
                if nei != parent:
                    child_sum = dfs(node, nei)
                    if child_sum % k == 0:  # child is a separate component
                        components += 1
                    else:  # child should combine with parent
                        parent_sum += child_sum
            return parent_sum

        dfs(-1, 0)
        return components


s = Solution()
print(s.maxKDivisibleComponents(n=5, edges=[[0, 2], [1, 2], [1, 3], [2, 4]], values=[1, 8, 1, 4, 4], k=6))
print(
    s.maxKDivisibleComponents(n=7, edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], values=[3, 0, 6, 1, 5, 2, 1],
                              k=3))

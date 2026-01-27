from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node, col):
            color[node] = col
            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, not color[node]):
                        return False
                elif color[nei] == color[node]:
                    return False
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True


"""
- Color the graph with 2 colors such that no adjacent nodes have same color.
- Linear graph with no cycles are always bipartite.
- Any graph with even cycle length are always bipartite.
"""
# LeetCode 785
s = Solution()
print(s.isBipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(s.isBipartite(graph=[[1, 3], [0, 2], [1, 3], [0, 2]]))

from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def bfs(start):
            q = deque()
            q.append(start)
            color[start] = 0

            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = not color[node]
                        q.append(nei)
                    elif color[nei] == color[node]:
                        return False
            return True

        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True


"""
- Color the graph with 2 colors such that no adjacent nodes have same color.
- Linear graph with no cycles are always bipartite.
- Any graph with even cycle length are always bipartite.
"""
s = Solution()
print(s.isBipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(s.isBipartite(graph=[[1, 3], [0, 2], [1, 3], [0, 2]]))

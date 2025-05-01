from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        in_degree = [0] * n
        graph_rev = [[] for _ in range(n)]
        for i in range(n):
            for nei in graph[i]:
                graph_rev[nei].append(i)
                in_degree[i] += 1

        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph_rev[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        res.sort()
        return res


s = Solution()
print(s.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]))
print(s.eventualSafeNodes(graph=[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))

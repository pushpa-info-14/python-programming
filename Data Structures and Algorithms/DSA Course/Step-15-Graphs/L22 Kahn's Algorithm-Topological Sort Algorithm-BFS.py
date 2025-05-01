"""
- Linear ordering of vertices such that if there is an edge between u & v, u appears before v in their ordering
- DAG(Directed Acyclic Graph)
"""
from collections import deque


def topologicalSort(graph):
    n = len(graph)
    in_degree = [0] * n

    for i in range(n):
        for nei in graph[i]:
            in_degree[nei] += 1

    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                q.append(nei)
    return res


print(topologicalSort([[], [], [3], [1], [0, 1], [0, 2]]))

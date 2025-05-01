from typing import *


def topologicalSort(node, graph, visited, stack):
    visited.add(node)
    for v, w in graph[node]:
        if v not in visited:
            topologicalSort(v, graph, visited, stack)
    stack.append(node)


def shortestPathInDAG(n: int, m: int, edges: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append([v, w])

    visited = set()
    stack = []
    for i in range(n):
        if i not in visited:
            topologicalSort(i, graph, visited, stack)

    int_max = 10 ** 9
    distance = [int_max] * n
    distance[0] = 0
    while stack:
        node = stack.pop()
        for v, w in graph[node]:
            if distance[node] + w < distance[v]:
                distance[v] = distance[node] + w

    for i in range(n):
        if distance[i] == int_max:
            distance[i] = -1
    return distance


print(shortestPathInDAG(3, 3, [[0, 1, 2], [1, 2, 3], [0, 2, 6]]))

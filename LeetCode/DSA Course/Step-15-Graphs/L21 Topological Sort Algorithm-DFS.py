"""
- Linear ordering of vertices such that if there is an edge between u & v, u appears before v in their ordering
- DAG(Directed Acyclic Graph)
"""


def topologicalSort(graph):
    n = len(graph)
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)
        stack.append(node)

    for i in range(n):
        if i not in visited:
            dfs(i)
    res = []
    while stack:
        res.append(stack.pop())
    return res


print(topologicalSort([[], [], [3], [1], [0, 1], [0, 2]]))

def detectCycle(graph):
    n = len(graph)
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei, node):
                    return True
            elif parent != nei:
                return True
        return False

    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False


print(detectCycle([[1], [2], [3], [4, 7], [5], [6], [], [5], [2, 9], [10], [8]]))
print(detectCycle([[1], [2], [3], [4], [5], [6], []]))

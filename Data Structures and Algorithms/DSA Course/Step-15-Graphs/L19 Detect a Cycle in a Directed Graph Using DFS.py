def detectCycle(graph):
    n = len(graph)
    visited = set()
    path_visited = set()

    def dfs(node):
        visited.add(node)
        path_visited.add(node)

        for nei in graph[node]:
            if nei not in visited:  # When the node is not visited
                if dfs(nei):
                    return True
            elif nei in path_visited:  # If the node is visited and path visited, it is a cycle
                return True

        path_visited.remove(node)
        return False

    for i in range(n):
        if i not in visited:
            if dfs(i):
                return True
    return False


print(detectCycle([[1], [2], [3], [4, 7], [5], [6], [], [5], [2, 9], [10], [8]]))
print(detectCycle([[1], [2], [3], [4], [5], [6], []]))

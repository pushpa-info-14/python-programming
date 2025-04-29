def detectCycle(n, adj):
    visited = set()
    path_visited = set()

    def dfs(node):
        visited.add(node)
        path_visited.add(node)

        for nei in adj[node]:
            if nei not in visited:  # When the node is not visited
                if dfs(nei):
                    return True
            elif nei in path_visited:  # If the node is visited and path visited, it is a cycle
                return True

        path_visited.remove(node)
        return False

    for i in range(1, n + 1):
        if i not in visited:
            if dfs(i):
                return True
    return False


print(detectCycle(n=9, adj={
    1: [2],
    2: [3],
    3: [4, 7],
    4: [5],
    5: [6],
    6: [],
    7: [5],
    8: [2, 9],
    9: [10],
    10: [8]
}))

print(detectCycle(n=6, adj={
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: [6],
    6: []
}))

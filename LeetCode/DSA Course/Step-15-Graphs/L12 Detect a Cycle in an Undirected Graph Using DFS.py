def detectCycle(n, adj):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nei in adj[node]:
            if nei not in visited:
                if dfs(nei, node):
                    return True
            elif parent != nei:
                return True
        return False

    for i in range(1, n + 1):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False


print(detectCycle(n=9, adj={
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2],
    5: [6],
    6: [5],
    7: [8, 9],
    8: [7, 9],
    9: [7, 8]
}))

print(detectCycle(n=6, adj={
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2],
    5: [6],
    6: [5]
}))

from collections import deque


def detectCycle(n, adj):
    visited = set()

    def bfs(src):
        q = deque()
        q.append((src, -1))
        visited.add(src)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei not in visited:
                    q.append((nei, node))
                    visited.add(nei)
                elif parent != nei:
                    return True
        return False

    for i in range(1, n + 1):
        if i not in visited:
            if bfs(i):
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

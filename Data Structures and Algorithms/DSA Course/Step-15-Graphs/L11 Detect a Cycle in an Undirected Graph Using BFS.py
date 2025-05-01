from collections import deque


def detectCycle(graph):
    n = len(graph)
    visited = set()

    def bfs(src):
        q = deque()
        q.append((src, -1))
        visited.add(src)

        while q:
            node, parent = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    q.append((nei, node))
                    visited.add(nei)
                elif parent != nei:
                    return True
        return False

    for i in range(n):
        if i not in visited:
            if bfs(i):
                return True
    return False


print(detectCycle([[1], [2], [3], [4, 7], [5], [6], [], [5], [2, 9], [10], [8]]))
print(detectCycle([[1], [2], [3], [4], [5], [6], []]))

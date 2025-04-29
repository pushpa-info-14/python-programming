from collections import deque


def detectCycle(graph):
    n = len(graph)
    in_degree = [0] * n

    for i in range(n):
        for nei in graph[i]:
            in_degree[nei] += 1

    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    count = 0
    while q:
        node = q.popleft()
        count += 1
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                q.append(nei)
    return False if n == count else True


print(detectCycle([[1], [2], [3], [4, 7], [5], [6], [], [5], [2, 9], [10], [8]]))
print(detectCycle([[1], [2], [3], [4], [5], [6], []]))

from collections import deque
from typing import List


def shortestPath(src: int, graph: List[List[int]]):
    n = len(graph)
    int_max = 10 ** 9
    distance = [int_max] * n
    q = deque()
    distance[src] = 0
    q.append(src)

    while q:
        node = q.popleft()
        for nei in graph[node]:
            if distance[nei] > distance[node] + 1:
                distance[nei] = distance[node] + 1
                q.append(nei)

    for i in range(n):
        if distance[i] == int_max:
            distance[i] = -1
    return distance


print(shortestPath(0, [[1, 3], [0, 2, 3], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [6, 7]]))

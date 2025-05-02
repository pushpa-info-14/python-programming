import heapq
from typing import List


def shortestPath(src: int, dest: int, graph: List[List[List[int]]]):
    n = len(graph)
    int_max = 10 ** 9
    distance = [int_max] * n
    parent = [-1] * n

    q = [(0, src)]
    distance[src] = 0
    parent[src] = src

    while q:
        dist, node = heapq.heappop(q)
        for nei, w in graph[node]:
            if distance[nei] > dist + w:
                distance[nei] = dist + w
                heapq.heappush(q, (dist + w, nei))
                parent[nei] = node

    if distance[dest] == int_max:
        return [-1]
    res = []
    node = dest
    while parent[node] != node:
        res.append(node)
        node = parent[node]
    res.append(src)
    res.reverse()
    return res


"""
Dijkstra's algorithm does not work when there is a negative edge or cycle

TC -> ElogV
"""

print(shortestPath(0, 4, [
    [[1, 4], [2, 4]],
    [[0, 4], [2, 2]],
    [[0, 4], [1, 2], [3, 3], [4, 1], [5, 6]],
    [[2, 3], [5, 2]],
    [[2, 1], [5, 3]],
    [[2, 6], [3, 2], [4, 3]]
]))

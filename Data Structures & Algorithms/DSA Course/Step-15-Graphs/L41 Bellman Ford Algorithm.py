from typing import List


def shortestPath(n: int, edges: List[List[int]], src: int) -> List[int]:
    int_max = 10 ** 8
    distance = [int_max] * n
    distance[src] = 0
    for i in range(n - 1):
        count = 0
        for u, v, w in edges:
            if distance[u] != int_max and distance[v] > distance[u] + w: # u must be reachable
                distance[v] = distance[u] + w
                count += 1
        if count == 0:
            return distance
    for u, v, w in edges:
        if distance[u] != int_max and distance[v] > distance[u] + w: # u must be reachable
            return [-1]

    return distance


"""
Dijkstra's algorithm cannot handle negative edges and cycles.

Bellman Ford works on a directed graph.
Relax all the edges n-1 times sequentially.

TC O(VE)
"""

print(shortestPath(6, [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]], 0))
print(shortestPath(8, [[1, 0, -4], [3, 5, -4], [4, 3, -5], [5, 3, -10]], 1))

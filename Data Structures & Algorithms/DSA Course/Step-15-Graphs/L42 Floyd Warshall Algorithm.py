from typing import List


class Solution:
    def floydWarshall(self, dist: List[List[int]]):
        int_max = 10 ** 8
        n = len(dist)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != int_max and dist[k][j] != int_max:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        print(dist)


"""
Floyd–Warshall algorithm is an algorithm for finding the shortest paths in a
directed weighted graph with positive or negative edge weights. A single
execution of the algorithm will find the lengths of shortest paths between
all pairs of vertices.

Detect negative cycles. 
"""

inf = 10 ** 8
s = Solution()
s.floydWarshall([
    [0, 4, inf, 5, inf],
    [inf, 0, 1, inf, 6],
    [2, inf, 0, 3, inf],
    [inf, inf, 1, 0, 2],
    [1, inf, inf, 4, 0]])
s.floydWarshall([
    [0, 8, 7, -3],
    [1, 0, -1, 6],
    [6, 5, 0, 3],
    [inf, inf, inf, 0]
])

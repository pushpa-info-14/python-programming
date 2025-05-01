"""
n-nodes, m-edges
5, 6
[2,1],[1,3],[2,4],[3,4],[2,5],[4,5]
Adjacency Matrix
Adjacency List
"""
from collections import defaultdict

n = 5
edges = [[2, 1], [1, 3], [2, 4], [3, 4], [2, 5], [4, 5]]

adj = [[0] * (n + 1) for _ in range(n + 1)]
for u, v in edges:
    adj[u][v] = 1
    adj[v][u] = 1
print(adj)

adj_list = defaultdict(list)
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)
print(adj_list)

# Weighted Graph
edges = [[2, 1, 2], [1, 3, 3], [2, 4, 1], [3, 4, 4], [2, 5, 6], [4, 5, 3]]

adj = [[0] * (n + 1) for _ in range(n + 1)]
for u, v, w in edges:
    adj[u][v] = w
    adj[v][u] = w
print(adj)

adj_list = defaultdict(list)
for u, v, w in edges:
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))
print(adj_list)
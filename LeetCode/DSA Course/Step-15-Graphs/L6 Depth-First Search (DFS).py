from collections import defaultdict

n = 8
edges = [[1, 2], [1, 6], [2, 3], [2, 4], [6, 7], [6, 8], [4, 5], [7, 5]]

adj = defaultdict(list)

for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)


def dfs(node):
    visited.add(node)
    res.append(node)
    for nei in adj[node]:
        if nei not in visited:
            dfs(nei)


visited = set()
res = []
for i in range(1, n + 1):
    if i not in visited:
        dfs(i)

print(res)

# TC O(N) + O(2E)
# SC O(N) + O(N) + O(N)


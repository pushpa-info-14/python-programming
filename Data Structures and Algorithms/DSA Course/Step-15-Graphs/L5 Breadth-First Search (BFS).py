from collections import defaultdict, deque

edges = [[1, 2], [1, 6], [2, 3], [2, 4], [6, 7], [6, 8], [4, 5], [7, 5]]

adj = defaultdict(list)

for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

starting_node = 1
visited = set()
res = []
q = deque()

res.append(starting_node)
visited.add(starting_node)
for v in adj[starting_node]:
    q.append(v)
    visited.add(v)

while q:
    v = q.popleft()
    res.append(v)
    for nei in adj[v]:
        if nei not in visited:
            q.append(nei)
            visited.add(nei)

print(res)

# TC O(N) + O(2E)
# SC O(N) + O(N)

"""
Strongly Connected Components - SCC

Only valid for directed graphs.

1. Sort all the edges according to finishing time
2. Reverse the edges
3. Do a DFS
"""


class Solution:
    def dfs1(self, node, adj, visited, stack):
        visited[node] = 1
        for nei in adj[node]:
            if not visited[nei]:
                self.dfs1(nei, adj, visited, stack)
        stack.append(node)

    def dfs2(self, node, adj, visited):
        visited[node] = 1
        for nei in adj[node]:
            if not visited[nei]:
                self.dfs2(nei, adj, visited)

    def kosaraju(self, adj):
        n = len(adj)
        visited = [0] * n
        stack = []

        for i in range(n):
            if not visited[i]:
                self.dfs1(i, adj, visited, stack)

        adj_reversed = [[] for _ in range(n)]
        for i in range(n):
            visited[i] = 0
            for nei in adj[i]:
                adj_reversed[nei].append(i)

        scc = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                self.dfs2(node, adj_reversed, visited)
                scc += 1

        return scc


s = Solution()
print(s.kosaraju([[2, 3], [0], [1], [4], []]))  # 3
print(s.kosaraju([[1], [2], [0]]))  # 1
print(s.kosaraju([[1], []]))  # 2

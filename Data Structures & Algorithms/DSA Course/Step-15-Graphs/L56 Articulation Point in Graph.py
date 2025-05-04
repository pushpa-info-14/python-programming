class Solution:
    def __init__(self):
        self.timer = 1

    def articulationPoints(self, V, adj):
        n = V
        visited = [0] * n
        t_in = [0] * n
        t_low = [0] * n
        mark = [0] * n
        self.timer = 1

        def dfs(node, parent):
            visited[node] = 1
            t_in[node] = self.timer
            t_low[node] = self.timer
            self.timer += 1
            children = 0
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not visited[nei]:
                    dfs(nei, node)
                    t_low[node] = min(t_low[node], t_low[nei])
                    if t_low[nei] >= t_in[node] and parent != -1:
                        mark[node] = 1
                    children += 1
                else:
                    t_low[node] = min(t_low[node], t_in[nei])
            if children > 1 and parent == -1:
                mark[node] = 1

        for i in range(n):
            if not visited[i]:
                dfs(i, -1)

        res = []
        for i in range(n):
            if mark[i]:
                res.append(i)
        if len(res) == 0:
            return [-1]
        return res


"""
In graph theory, the root of a DFS (Depth-First Search) tree is an articulation point
(or cut vertex) if and only if it has at least two children in the DFS tree.
"""
s = Solution()
print(s.articulationPoints(5, [[1], [0, 4], [3, 4], [2, 4], [1, 2]]))

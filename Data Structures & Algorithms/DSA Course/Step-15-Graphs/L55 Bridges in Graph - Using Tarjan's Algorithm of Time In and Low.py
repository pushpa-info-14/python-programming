from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.timer = 1

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * n
        t_in = [0] * n
        t_low = [0] * n
        bridges = []
        self.timer = 1

        def dfs(node, parent):
            visited[node] = 1
            t_in[node] = self.timer
            t_low[node] = self.timer
            self.timer += 1
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not visited[nei]:
                    dfs(nei, node)
                    t_low[node] = min(t_low[node], t_low[nei])
                    if t_low[nei] > t_in[node]:
                        bridges.append([node, nei])
                else:
                    t_low[node] = min(t_low[node], t_low[nei])

        dfs(0, -1)
        return bridges


s = Solution()
print(s.criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))
print(s.criticalConnections(n=2, connections=[[0, 1]]))

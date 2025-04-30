from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n
        path_visited = [False] * n
        is_safe = [False] * n

        def dfs(node):
            visited[node] = True
            path_visited[node] = True
            is_safe[node] = False
            for nei in graph[node]:
                if not visited[nei]:
                    if not dfs(nei):
                        return False
                elif path_visited[nei]:
                    return False

            path_visited[node] = False
            is_safe[node] = True
            return True

        res = []
        for i in range(n):
            if not visited[i]:
                dfs(i)
        for i in range(n):
            if is_safe[i]:
                res.append(i)
        return res


s = Solution()
print(s.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]))
print(s.eventualSafeNodes(graph=[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))

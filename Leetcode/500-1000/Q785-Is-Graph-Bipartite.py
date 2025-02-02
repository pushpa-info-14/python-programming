from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        odd = [0] * n  # map node i -> odd=1, even=-1

        def bfs(i):
            if odd[i]:
                return True
            q = deque([i])
            odd[i] = -1
            while q:
                i = q.popleft()
                for nei in graph[i]:
                    if odd[i] == odd[nei]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[i]
            return True

        for i in range(n):
            if not bfs(i):
                return False
        return True


s = Solution()
print(s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))

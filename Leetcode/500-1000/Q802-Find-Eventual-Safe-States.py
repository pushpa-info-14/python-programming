from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        res = []

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False  # safe[i]
            safe[i] = True
            return True  # safe[i]

        for i in range(n):
            if dfs(i):
                res.append(i)

        return res


s = Solution()
print(s.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
print(s.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))

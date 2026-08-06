from collections import defaultdict
from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for u, v in invocations:
            edges[u].append(v)

        suspicious = set()

        def mark(node):
            suspicious.add(node)
            for nei in edges[node]:
                if nei not in suspicious:
                    mark(nei)

        mark(k)
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return [i for i in range(n)]

        return [i for i in range(n) if i not in suspicious]


s = Solution()
print(s.remainingMethods(n=4, k=1, invocations=[[1, 2], [0, 1], [3, 2]]))
print(s.remainingMethods(n=5, k=0, invocations=[[1, 2], [0, 2], [0, 1], [3, 4]]))
print(s.remainingMethods(n=3, k=2, invocations=[[1, 2], [0, 1], [2, 0]]))
print(s.remainingMethods(n=3, k=2, invocations=[[1, 0], [2, 0]]))  # [0, 1, 2]

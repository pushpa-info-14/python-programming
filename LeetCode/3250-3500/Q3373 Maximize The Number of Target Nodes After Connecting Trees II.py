from collections import defaultdict, deque, Counter
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def calculate(edges):
            adj_list = defaultdict(list)

            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)

            q = deque()
            q.append(0)
            colors = [-1] * (len(edges) + 1)
            colors[0] = 0

            while q:
                node = q.popleft()

                for nei in adj_list[node]:
                    if colors[nei] == -1:
                        colors[nei] = (colors[node] + 1) % 2
                        q.append(nei)

            return colors

        colors1 = calculate(edges1)
        colors2 = calculate(edges2)
        f1 = Counter(colors1)
        f2 = Counter(colors2)
        max2 = max(f2.values())

        n = len(edges1) + 1
        res = []
        for i in range(n):
            res.append(f1[colors1[i]] + max2)

        return res


s = Solution()
print(s.maxTargetNodes(edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
                       edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]))
print(s.maxTargetNodes(edges1=[[0, 1], [0, 2], [0, 3], [0, 4]], edges2=[[0, 1], [1, 2], [2, 3]]))
print(s.maxTargetNodes(edges1=[[0, 1]], edges2=[[0, 1]]))

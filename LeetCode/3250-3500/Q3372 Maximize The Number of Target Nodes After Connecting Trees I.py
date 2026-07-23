from collections import defaultdict, deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        int_max = 10 ** 9
        n = len(edges1) + 1
        m = len(edges2) + 1

        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        def calculate(size, src, max_distance, adj):
            q = deque()
            q.append((src, 0))
            distance = [int_max] * size
            distance[src] = 0

            while q:
                cur_node, cur_distance = q.popleft()
                if cur_distance > max_distance:
                    continue
                for nei in adj[cur_node]:
                    if distance[nei] > cur_distance + 1:
                        distance[nei] = cur_distance + 1
                        q.append((nei, cur_distance + 1))

            count = 0
            for d in distance:
                if d <= max_distance:
                    count += 1

            return count

        res1 = [0] * n
        res2 = [0] * m

        for i in range(n):
            res1[i] = calculate(n, i, k, adj1)

        for i in range(m):
            res2[i] = calculate(m, i, k - 1, adj2)

        max2 = max(res2)
        for i in range(n):
            res1[i] += max2

        return res1


s = Solution()
print(s.maxTargetNodes(edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
                       edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]], k=2))
print(s.maxTargetNodes(edges1=[[0, 1], [0, 2], [0, 3], [0, 4]], edges2=[[0, 1], [1, 2], [2, 3]], k=1))
print(s.maxTargetNodes(edges1=[[0, 1]], edges2=[[0, 1]], k=0))

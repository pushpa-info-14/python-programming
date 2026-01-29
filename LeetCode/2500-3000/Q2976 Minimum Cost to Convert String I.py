import heapq
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(len(original)):
            adj[original[i]].append((changed[i], cost[i]))

        @cache
        def bfs(s, t):
            visited = {s}
            q = [(0, s)]
            while q:
                dist, node = heapq.heappop(q)
                visited.add(node)
                if node == t:
                    return dist
                for nei, w in adj[node]:
                    if nei not in visited:
                        heapq.heappush(q, (dist + w, nei))
            return -1

        res = 0
        for i in range(len(source)):
            cur = bfs(source[i], target[i])
            if cur == -1:
                return -1
            res += cur
        return res


s = Solution()
print(s.minimumCost(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                    changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20]))
print(s.minimumCost(source="aaaa", target="bbbb", original=["a", "c"], changed=["c", "b"], cost=[1, 2]))
print(s.minimumCost(source="abcd", target="abce", original=["a"], changed=["e"], cost=[10000]))
print(s.minimumCost(source="aabbddccbc", target="abbbaabaca", original=["a", "b", "c", "b", "a", "d"],
                    changed=["d", "c", "b", "d", "b", "b"], cost=[3, 8, 7, 6, 7, 10]))

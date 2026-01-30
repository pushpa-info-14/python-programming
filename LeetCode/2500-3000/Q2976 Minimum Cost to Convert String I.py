import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = 10 ** 10
        adj = defaultdict(list)
        for i in range(len(original)):
            adj[ord(original[i]) - ord("a")].append((ord(changed[i]) - ord("a"), cost[i]))

        def dijkstra(s):
            d = [inf] * 26
            d[s] = 0
            q = [(0, s)]
            while q:
                dist, node = heapq.heappop(q)
                for nei, w in adj[node]:
                    if dist + w < d[nei]:
                        d[nei] = dist + w
                        heapq.heappush(q, (dist + w, nei))
            return d

        min_costs = [dijkstra(i) for i in range(26)]

        res = 0
        for i in range(len(source)):
            s = ord(source[i]) - ord("a")
            t = ord(target[i]) - ord("a")
            if min_costs[s][t] == inf:
                return -1
            res += min_costs[s][t]
        return res


s = Solution()
print(s.minimumCost(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                    changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20]))
print(s.minimumCost(source="aaaa", target="bbbb", original=["a", "c"], changed=["c", "b"], cost=[1, 2]))
print(s.minimumCost(source="abcd", target="abce", original=["a"], changed=["e"], cost=[10000]))
print(s.minimumCost(source="aabbddccbc", target="abbbaabaca", original=["a", "b", "c", "b", "a", "d"],
                    changed=["d", "c", "b", "d", "b", "b"], cost=[3, 8, 7, 6, 7, 10]))

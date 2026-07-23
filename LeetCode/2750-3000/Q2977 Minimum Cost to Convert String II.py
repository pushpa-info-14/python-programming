import heapq
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = 10 ** 10
        adj = defaultdict(list)
        for u, v, w in zip(original, changed, cost):
            adj[u].append((v, w))

        @cache
        def dijkstra(s, t):
            d = defaultdict(lambda: inf)
            d[s] = 0
            q = [(0, s)]  # (dist, node)
            while q:
                dist, node = heapq.heappop(q)
                for nei, w in adj[node]:
                    if dist + w < d[nei]:
                        d[nei] = dist + w
                        heapq.heappush(q, (dist + w, nei))
            return d[t]

        lengths = sorted(set(len(word) for word in original))

        @cache
        def dp(i):
            if i == len(source):
                return 0
            if source[i] == target[i]:  # Try next c and length
                best = dp(i + 1)
            else:  # Try lengths
                best = inf
            for length in lengths:
                if i + length > len(source):
                    break
                s = source[i: i + length]
                t = target[i:i + length]
                if s not in adj:
                    continue
                best = min(best, dijkstra(s, t) + dp(i + length))
            return best

        res = dp(0)
        return res if res != inf else -1


solution = Solution()
print(solution.minimumCost(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                           changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20]))
print(solution.minimumCost(source="abcdefgh", target="acdeeghh", original=["bcd", "fgh", "thh"], changed=["cde", "thh", "ghh"],
                           cost=[1, 3, 5]))
print(solution.minimumCost(source="abcdefgh", target="addddddd", original=["bcd", "defgh"], changed=["ddd", "ddddd"],
                           cost=[100, 1578]))

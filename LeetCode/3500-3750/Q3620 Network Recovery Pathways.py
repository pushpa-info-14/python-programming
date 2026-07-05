import heapq
from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        adj = defaultdict(list)
        n = len(online)
        min_d = inf
        max_d = -inf
        for u, v, w in edges:
            min_d = min(min_d, w)
            max_d = max(max_d, w)
            if online[u] and online[v]:
                adj[u].append((v, w))

        def check(minimum):
            dist = [k + 1] * n
            dist[0] = 0
            q = [(0, 0)]  # dist, node
            while q:
                cur, node = heapq.heappop(q)
                if node == n - 1:
                    return True
                if cur > dist[node]:
                    continue
                for nei, d in adj[node]:
                    if d < minimum:
                        continue
                    nd = d + cur
                    if nd < dist[nei]:
                        dist[nei] = nd
                        heapq.heappush(q, (nd, nei))
            return False

        res = -1
        low, high = min_d, max_d
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res


s = Solution()
print(s.findMaxPathScore(edges=[[0, 1, 5], [1, 3, 10], [0, 2, 3], [2, 3, 4]], online=[True, True, True, True], k=10))
print(s.findMaxPathScore(edges=[[0, 1, 7], [1, 4, 5], [0, 2, 6], [2, 3, 6], [3, 4, 2], [2, 4, 6]],
                         online=[True, True, True, False, True], k=12))

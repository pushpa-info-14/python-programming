import math
from collections import defaultdict
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        time_at = [-1 for _ in range(n)]

        def move_bob(src, prev, t):
            if src == 0:
                time_at[src] = t
                return True

            for nei in adj[src]:
                if nei == prev:
                    continue
                if move_bob(nei, src, t + 1):
                    time_at[src] = t
                    return True
            return False

        def move_alice(src, prev, t, reward):
            if time_at[src] == t:
                reward += amount[src] // 2
            elif time_at[src] > t or time_at[src] == -1:
                reward += amount[src]

            if src != 0 and len(adj[src]) == 1:
                return reward

            res = -math.inf
            for nei in adj[src]:
                if nei == prev:
                    continue
                res = max(res, move_alice(nei, src, t + 1, reward))
            return res

        move_bob(bob, -1, 0)
        # print(time_at)
        return move_alice(0, -1, 0, 0)


s = Solution()
print(s.mostProfitablePath([[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6]))  # 6
print(s.mostProfitablePath([[0, 1]], 1, [-7280, 2350]))  # -7280
print(s.mostProfitablePath([[0, 1], [1, 2], [2, 3]], 3, [-5644, -6018, 1188, -8502]))  # -11662
print(s.mostProfitablePath([[0, 2], [0, 5], [1, 3], [1, 5], [2, 4]], 4, [5018, 8388, 6224, 3466, 3808, 3456]))  # 20328
print(s.mostProfitablePath([[0, 2], [0, 6], [1, 3], [1, 5], [2, 5], [4, 6]], 6,
                           [8838, -6396, -5940, 2694, -1366, 4616, 2966]))  # 7472
print(s.mostProfitablePath([[0, 2], [1, 4], [1, 6], [2, 4], [3, 6], [3, 7], [5, 7]], 4,
                           [-6896, -1216, -1208, -1108, 1606, -7704, -9212, -8258]))  # -34998

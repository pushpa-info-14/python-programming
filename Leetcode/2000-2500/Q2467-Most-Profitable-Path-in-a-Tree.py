import math
from collections import defaultdict
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        adj = defaultdict(list)
        visited = set()
        visited2 = set()
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        time_at = [-1] * n

        def move_bob(at, income, time):
            time_at[at] = time
            if at == 0:
                return True

            visited2.add(at)

            end = True
            for nei in adj[at]:
                if nei not in visited2:
                    end = False
            if end:
                return False

            for nei in adj[at]:
                if nei not in visited2:
                    if move_bob(nei, income, time + 1):
                        return True
                    else:
                        time_at[nei] = -1
                        visited2.remove(nei)

        def move_alice(at, income, time):
            if time_at[at] == time:
                income += amount[at] // 2
            elif time_at[at] > time or time_at[at] == -1:
                income += amount[at]

            visited.add(at)

            end = True
            for nei in adj[at]:
                if nei not in visited:
                    end = False
            if end:
                return income

            res = -math.inf
            for nei in adj[at]:
                if nei not in visited:
                    res = max(res, move_alice(nei, income, time + 1))

            return res

        move_bob(bob, 0, 0)
        # print(time_at)
        # print(visited2)
        return move_alice(0, 0, 0)


s = Solution()
print(s.mostProfitablePath([[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6]))  # 6
print(s.mostProfitablePath([[0, 1]], 1, [-7280, 2350]))  # -7280
print(s.mostProfitablePath([[0, 1], [1, 2], [2, 3]], 3, [-5644, -6018, 1188, -8502]))  # -11662
print(s.mostProfitablePath([[0, 2], [0, 5], [1, 3], [1, 5], [2, 4]], 4, [5018, 8388, 6224, 3466, 3808, 3456]))  # 20328
print(s.mostProfitablePath([[0, 2], [0, 6], [1, 3], [1, 5], [2, 5], [4, 6]], 6,
                           [8838, -6396, -5940, 2694, -1366, 4616, 2966]))  # 7472
print(s.mostProfitablePath([[0, 2], [1, 4], [1, 6], [2, 4], [3, 6], [3, 7], [5, 7]], 4,
                           [-6896, -1216, -1208, -1108, 1606, -7704, -9212, -8258]))  # -34998

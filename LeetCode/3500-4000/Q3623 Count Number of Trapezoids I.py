from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        y_planes = defaultdict(int)
        for x, y in points:
            y_planes[y] += 1
        pairs = []
        for n in y_planes.values():
            if n > 1:
                pairs.append((n * (n - 1)) // 2)
        total_pairs = sum(pairs)
        res = 0
        for x in pairs:
            res += x * (total_pairs - x)
        res //= 2
        return res % mod

    def countTrapezoids2(self, points: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        intercepts = defaultdict(int)
        for point in points:
            intercepts[point[1]] += 1
        total_sum = 0
        res = 0
        for x in intercepts.values():
            edge = x * (x - 1) // 2
            res = (res + edge * total_sum) % mod
            total_sum = (total_sum + edge) % mod
        return res


s = Solution()
print(s.countTrapezoids(points=[[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
print(s.countTrapezoids(points=[[0, 0], [1, 0], [0, 1], [2, 1]]))
print(s.countTrapezoids2(points=[[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
print(s.countTrapezoids2(points=[[0, 0], [1, 0], [0, 1], [2, 1]]))

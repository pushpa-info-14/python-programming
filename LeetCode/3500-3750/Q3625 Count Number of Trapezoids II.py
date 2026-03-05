from collections import defaultdict
from typing import List


def gcd(a, b):
    while a and b:
        a, b = b, a % b
    return a


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10 ** 9 + 7
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        res = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2
                # y = mx + c
                # m = slope
                # c = intercept
                if x2 == x1:
                    m = inf
                    c = x1
                else:
                    m = (y2 - y1) / (x2 - x1)
                    c = (y1 * dx - x1 * dy) / dx

                mid = (x1 + x2) * 10000 + (y1 + y2)
                slope_to_intercept[m].append(c)
                mid_to_slope[mid].append(m)

        for intercepts in slope_to_intercept.values():
            if len(intercepts) == 1:
                continue

            counter = defaultdict(int)
            for intercept in intercepts:
                counter[intercept] += 1

            total_sum = 0
            for count in counter.values():
                res += total_sum * count
                total_sum += count

        for slopes in mid_to_slope.values():
            if len(slopes) == 1:
                continue

            counter = defaultdict(int)
            for slop in slopes:
                counter[slop] += 1

            total_sum = 0
            for count in counter.values():
                res -= total_sum * count
                total_sum += count

        return res


s = Solution()
print(s.countTrapezoids(points=[[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]))
print(s.countTrapezoids(points=[[0, 0], [1, 0], [0, 1], [2, 1]]))

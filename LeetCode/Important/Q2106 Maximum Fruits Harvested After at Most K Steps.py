from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        start_index = bisect_left(fruits, [startPos, 0])

        distance_right = []
        prefix_sum_right = []
        for i in range(start_index, n):
            pos, fruit_count = fruits[i]
            distance_right.append(pos - startPos)
            prefix_sum_right.append(fruit_count + (0 if not prefix_sum_right else prefix_sum_right[-1]))

        distances_left = []
        prefix_sum_left = []
        for i in range(start_index - 1, -1, -1):
            pos, fruit_count = fruits[i]
            distances_left.append(startPos - pos)
            prefix_sum_left.append(fruit_count + (0 if not prefix_sum_left else prefix_sum_left[-1]))

        def solve(d1, total1, d2, total2):
            best = 0
            for i, d in enumerate(d1):
                if d > k:
                    break
                count = total1[i]
                if k - (2 * d) >= 0:
                    i2 = bisect_right(d2, k - (2 * d))
                    if i2 > 0:
                        count += total2[i2 - 1]
                best = max(best, count)
            return best

        return max(
            solve(distance_right, prefix_sum_right, distances_left, prefix_sum_left),
            solve(distances_left, prefix_sum_left, distance_right, prefix_sum_right))


s = Solution()
print(s.maxTotalFruits(fruits=[[2, 8], [6, 3], [8, 6]], startPos=5, k=4))
print(s.maxTotalFruits(fruits=[[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], startPos=5, k=4))
print(s.maxTotalFruits(fruits=[[0, 3], [6, 4], [8, 5]], startPos=3, k=2))

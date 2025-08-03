from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        N = len(fruits)
        start_index = bisect_left(fruits, [startPos, 0])

        distances1 = []
        total_fruits1 = []
        for i in range(start_index, N):
            pos, fruit_count = fruits[i]
            distances1.append(pos - startPos)
            total_fruits1.append(fruit_count + (0 if not total_fruits1 else total_fruits1[-1]))

        distances2 = []
        total_fruits2 = []
        for i in range(start_index - 1, -1, -1):
            pos, fruit_count = fruits[i]
            distances2.append(startPos - pos)
            total_fruits2.append(fruit_count + (0 if not total_fruits2 else total_fruits2[-1]))

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
            solve(distances1, total_fruits1, distances2, total_fruits2),
            solve(distances2, total_fruits2, distances1, total_fruits1))


s = Solution()
print(s.maxTotalFruits(fruits=[[2, 8], [6, 3], [8, 6]], startPos=5, k=4))
print(s.maxTotalFruits(fruits=[[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], startPos=5, k=4))
print(s.maxTotalFruits(fruits=[[0, 3], [6, 4], [8, 5]], startPos=3, k=2))

from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sort by x asc, and for equal x sort by y desc
        points.sort(key=lambda p: (p[0], -p[1]))

        n = len(points)
        count = 0
        for A in range(n - 1):
            bottom_right_y = -10 ** 18
            for B in range(A + 1, n):
                if points[A][1] >= points[B][1] > bottom_right_y:
                    count += 1
                    bottom_right_y = points[B][1]
        return count


s = Solution()
print(s.numberOfPairs(points=[[1, 1], [2, 2], [3, 3]]))
print(s.numberOfPairs(points=[[6, 2], [4, 4], [2, 6]]))
print(s.numberOfPairs(points=[[3, 1], [1, 3], [1, 1]]))

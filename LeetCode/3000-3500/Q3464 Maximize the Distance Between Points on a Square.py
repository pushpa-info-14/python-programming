import bisect
from typing import List


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        n = len(points)
        flatten = []  # Distance from (0, 0)

        for x, y in points:
            if y == 0:
                flatten.append(x)
            elif y == side:
                flatten.append(side * 2 + (side - x))
            elif x == 0:
                flatten.append(side * 3 + (side - y))
            elif x == side:
                flatten.append(side + y)
        flatten.sort()

        def check(distance):
            for i in range(n):
                count = 1
                cur = i
                while count < k:
                    jump = bisect.bisect_left(flatten, flatten[cur] + distance)
                    if jump == len(flatten):
                        return False
                    if flatten[i] + 4 * side - flatten[jump] < distance:
                        break
                    count += 1
                    cur = jump
                if count == k:
                    return True
            return False

        low, high = 1, side
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high


s = Solution()
print(s.maxDistance(side=2, points=[[0, 2], [2, 0], [2, 2], [0, 0]], k=4))
print(s.maxDistance(side=2, points=[[0, 0], [1, 2], [2, 0], [2, 2], [2, 1]], k=4))
print(s.maxDistance(side=2, points=[[0, 0], [0, 1], [0, 2], [1, 2], [2, 0], [2, 2], [2, 1]], k=5))
print(s.maxDistance(side=15, points=[[15, 6], [0, 13], [13, 0], [10, 0]], k=4))

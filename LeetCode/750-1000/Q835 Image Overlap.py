from collections import Counter
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        l1 = [(x, y) for x in range(n) for y in range(n) if img1[x][y]]
        l2 = [(x, y) for x in range(n) for y in range(n) if img2[x][y]]
        f = Counter()

        for x1, y1 in l1:
            for x2, y2 in l2:
                dx, dy = x2 - x1, y2 - y1
                f[(dx, dy)] += 1

        return max(f.values(), default=0)


s = Solution()
print(s.largestOverlap(img1=[[1, 1, 0], [0, 1, 0], [0, 1, 0]], img2=[[0, 0, 0], [0, 1, 1], [0, 0, 1]]))
print(s.largestOverlap(img1=[[1]], img2=[[1]]))
print(s.largestOverlap(img1=[[0]], img2=[[0]]))

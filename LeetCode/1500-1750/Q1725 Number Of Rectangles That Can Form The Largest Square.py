from collections import Counter
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l = [min(x, y) for x, y in rectangles]
        max_l = max(l)
        counter = Counter(l)
        return counter[max_l]

    def countGoodRectangles2(self, rectangles: List[List[int]]) -> int:
        max_l = 0
        res = 0
        for x, y in rectangles:
            square_l = min(x, y)
            if square_l > max_l:
                max_l = square_l
                res = 1
            elif square_l == max_l:
                res += 1
        return res


s = Solution()
print(s.countGoodRectangles(rectangles=[[5, 8], [3, 9], [5, 12], [16, 5]]))
print(s.countGoodRectangles(rectangles=[[2, 3], [3, 7], [4, 3], [3, 7]]))
print(s.countGoodRectangles2(rectangles=[[5, 8], [3, 9], [5, 12], [16, 5]]))
print(s.countGoodRectangles2(rectangles=[[2, 3], [3, 7], [4, 3], [3, 7]]))

from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rects = sorted([rec1, rec2])
        ax1, ay1, ax2, ay2 = rects[0]
        bx1, by1, bx2, by2 = rects[1]
        if ax2 <= bx1 or ay2 <= by1 or ax1 >= bx2 or ay1 >= by2:
            return False
        return True


s = Solution()
print(s.isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3]))
print(s.isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1]))
print(s.isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[2, 2, 3, 3]))
print(s.isRectangleOverlap(rec1=[7, 8, 13, 15], rec2=[10, 8, 12, 20]))

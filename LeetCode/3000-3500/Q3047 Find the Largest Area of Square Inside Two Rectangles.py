from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        width = 0
        for i in range(n):
            xbl1, ybl1 = bottomLeft[i]
            xtr1, ytr1 = topRight[i]
            for j in range(i + 1, n):
                xbl2, ybl2 = bottomLeft[j]
                xtr2, ytr2 = topRight[j]
                if xtr1 <= xbl2 or ytr1 <= ybl2:
                    continue
                l = max(xbl1, xbl2)
                r = min(xtr1, xtr2)
                b = max(ybl1, ybl2)
                t = min(ytr1, ytr2)
                cur = min(r - l, t - b)
                width = max(width, cur)
        return width * width


s = Solution()
print(s.largestSquareArea(bottomLeft=[[1, 1], [2, 2], [3, 1]], topRight=[[3, 3], [4, 4], [6, 6]]))  # 1
print(s.largestSquareArea(bottomLeft=[[1, 1], [2, 2], [3, 1]], topRight=[[3, 3], [5, 4], [6, 6]]))  # 4
print(s.largestSquareArea(bottomLeft=[[1, 1], [1, 3], [1, 5]], topRight=[[5, 5], [5, 7], [5, 9]]))  # 4
print(s.largestSquareArea(bottomLeft=[[1, 1], [2, 2], [1, 2]], topRight=[[3, 3], [4, 4], [3, 4]]))  # 1
print(s.largestSquareArea(bottomLeft=[[1, 1], [3, 3], [3, 1]], topRight=[[2, 2], [4, 4], [4, 2]]))  # 0
print(s.largestSquareArea(bottomLeft=[[2, 2], [1, 3]], topRight=[[3, 4], [5, 5]]))  # 1
print(s.largestSquareArea(bottomLeft=[[4, 6], [1, 2], [7, 2]], topRight=[[9, 8], [5, 5], [8, 5]]))  # 0

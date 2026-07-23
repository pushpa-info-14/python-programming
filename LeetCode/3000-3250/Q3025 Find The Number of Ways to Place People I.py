from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                if x2 >= x1 and y2 <= y1:
                    is_valid = True
                    for k in range(n):
                        if i == k or j == k:
                            continue
                        x3, y3 = points[k]
                        if x1 <= x3 <= x2 and y1 >= y3 >= y2:
                            is_valid = False
                            break
                    if is_valid:
                        res += 1
        return res


s = Solution()
print(s.numberOfPairs(points=[[1, 1], [2, 2], [3, 3]]))
print(s.numberOfPairs(points=[[6, 2], [4, 4], [2, 6]]))
print(s.numberOfPairs(points=[[3, 1], [1, 3], [1, 1]]))
print(s.numberOfPairs(points=[[3, 1]]))
print(s.numberOfPairs(points=[[3, 1], [1, 3]]))

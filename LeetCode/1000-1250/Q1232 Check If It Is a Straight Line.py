from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        m = set()
        inf = 10 ** 9
        for i in range(1, len(coordinates)):
            x1, x2 = coordinates[i - 1][0], coordinates[i][0]
            y1, y2 = coordinates[i - 1][1], coordinates[i][1]
            if x2 - x1 == 0:
                m.add(inf)
            else:
                m.add((y2 - y1) / (x2 - x1))
        return len(m) == 1


s = Solution()
print(s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(s.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))

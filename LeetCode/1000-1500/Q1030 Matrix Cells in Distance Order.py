from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        values = []
        for r in range(rows):
            for c in range(cols):
                values.append([abs(r - rCenter) + abs(c - cCenter), r, c])
        values.sort()
        res = []
        for _, r, c in values:
            res.append([r, c])
        return res


s = Solution()
print(s.allCellsDistOrder(rows=1, cols=2, rCenter=0, cCenter=0))
print(s.allCellsDistOrder(rows=2, cols=2, rCenter=0, cCenter=1))
print(s.allCellsDistOrder(rows=2, cols=3, rCenter=1, cCenter=2))

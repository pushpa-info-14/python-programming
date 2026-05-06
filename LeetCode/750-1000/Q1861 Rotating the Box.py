from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        box = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                box[j][i] = boxGrid[m - 1 - i][j]
        for c in range(m):
            count = 0
            for r in range(n):
                if box[r][c] == '#':
                    box[r][c] = '.'
                    count += 1
                if box[r][c] == '*':
                    for i in range(r - count, r):
                        box[i][c] = '#'
                    count = 0
            if count:
                for i in range(n - count, n):
                    box[i][c] = '#'
        return box


s = Solution()
print(s.rotateTheBox(boxGrid=[["#", ".", "#"]]))
print(s.rotateTheBox(boxGrid=[["#", ".", "*", "."],
                              ["#", "#", "*", "."]]))
print(s.rotateTheBox(boxGrid=[["#", "#", "*", ".", "*", "."],
                              ["#", "#", "#", "*", ".", "."],
                              ["#", "#", "#", ".", "#", "."]]))

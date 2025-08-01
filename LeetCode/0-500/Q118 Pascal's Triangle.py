from typing import List


def pascalRow(row):
    res = []
    ans = 1
    res.append(ans)
    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // col
        res.append(ans)
    return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row in range(1, numRows + 1):
            res.append(pascalRow(row))
        return res


s = Solution()
print(s.generate(5))
print(s.generate(1))

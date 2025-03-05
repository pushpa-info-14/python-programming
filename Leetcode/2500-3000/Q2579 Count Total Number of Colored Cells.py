class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1

        for i in range(n):
            res += (4 * i)
        return res

    def coloredCells2(self, n: int) -> int:
        return 1 + 4 * (n - 1) * n // 2

s =Solution()
print(s.coloredCells(1))
print(s.coloredCells(2))
print(s.coloredCells2(1))
print(s.coloredCells2(2))
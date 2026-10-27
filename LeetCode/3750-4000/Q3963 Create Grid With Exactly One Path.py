class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []
        for _ in range(m - 1):
            res.append('.' + '#' * (n - 1))
        res.append('.' * n)
        return res


s = Solution()
print(s.createGrid(m=2, n=3))
print(s.createGrid(m=3, n=3))
print(s.createGrid(m=1, n=4))

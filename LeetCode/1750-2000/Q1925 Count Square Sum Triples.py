class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        squares = [i * i for i in range(1, n + 1)]
        seen = set(squares)
        for a in squares:
            for b in squares:
                if a + b in seen:
                    res += 1
        return res


s = Solution()
print(s.countTriples(5))
print(s.countTriples(10))

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1: return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, n, increment):
                res += s[i]
                if 0 < r < numRows - 1 and i + increment - 2 * r < n:
                    res += s[i + increment - 2 * r]

        return res


s = Solution()
print(s.convert("PAYPALISHIRING", 1))
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText) // rows
        grid = [[""] * n for _ in range(rows)]
        for i in range(len(encodedText)):
            grid[i // n][i % n] = encodedText[i]
        res = ""
        for c in range(n):
            for r in range(rows):
                if r + c < n:
                    res += grid[r][r + c]
        return res.rstrip()

    def decodeCiphertext2(self, encodedText: str, rows: int) -> str:
        n = len(encodedText) // rows
        res = ""
        for c in range(n):
            for r in range(rows):
                if r + c < n:
                    res += encodedText[r * n + r + c]
        return res.rstrip()


s = Solution()
print(s.decodeCiphertext(encodedText="ch   ie   pr", rows=3))
print(s.decodeCiphertext(encodedText="iveo    eed   l te   olc", rows=4))
print(s.decodeCiphertext(encodedText="coding", rows=1))
print("------")
print(s.decodeCiphertext2(encodedText="ch   ie   pr", rows=3))
print(s.decodeCiphertext2(encodedText="iveo    eed   l te   olc", rows=4))
print(s.decodeCiphertext2(encodedText="coding", rows=1))

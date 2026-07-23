class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        grid = [[""] * cols for _ in range(rows)]
        for i in range(len(encodedText)):
            grid[i // cols][i % cols] = encodedText[i]
        res = ""
        for c in range(cols):
            for r in range(rows):
                if r + c < cols:
                    res += grid[r][r + c]
        return res.rstrip()

    def decodeCiphertext2(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        res = ""
        for c in range(cols):
            for r in range(rows):
                if r + c < cols:
                    res += encodedText[r * cols + r + c]
        return res.rstrip()


s = Solution()
print(s.decodeCiphertext(encodedText="ch   ie   pr", rows=3))
print(s.decodeCiphertext(encodedText="iveo    eed   l te   olc", rows=4))
print(s.decodeCiphertext(encodedText="coding", rows=1))
print("------")
print(s.decodeCiphertext2(encodedText="ch   ie   pr", rows=3))
print(s.decodeCiphertext2(encodedText="iveo    eed   l te   olc", rows=4))
print(s.decodeCiphertext2(encodedText="coding", rows=1))

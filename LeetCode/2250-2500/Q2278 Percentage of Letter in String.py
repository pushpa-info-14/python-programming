class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int((s.count(letter) / len(s)) * 100)


s = Solution()
print(s.percentageLetter(s="foobar", letter="o"))
print(s.percentageLetter(s="jjjj", letter="k"))

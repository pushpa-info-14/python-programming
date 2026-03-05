class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        res = list(s)
        vowels = "aeiou"
        n = len(s)
        for i in range(n - 1, -1, -1):
            if res[i] in vowels:
                res.pop()
            else:
                break
        return "".join(res)


s = Solution()
print(s.trimTrailingVowels(s="idea"))
print(s.trimTrailingVowels(s="day"))
print(s.trimTrailingVowels(s="aeiou"))

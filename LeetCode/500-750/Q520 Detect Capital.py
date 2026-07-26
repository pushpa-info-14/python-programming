class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        count = 0
        for c in word:
            if c.isupper():
                count += 1
        if n == count or count == 0:
            return True
        if count == 1 and word[0].isupper():
            return True
        return False


s = Solution()
print(s.detectCapitalUse(word="USA"))
print(s.detectCapitalUse(word="FlaG"))

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        res = 0
        for word in words:
            can = True
            for c in word:
                if c in brokenLetters:
                    can = False
                    break
            if can:
                res += 1

        return res


s = Solution()
print(s.canBeTypedWords(text="hello world", brokenLetters="ad"))
print(s.canBeTypedWords(text="leet code", brokenLetters="lt"))
print(s.canBeTypedWords(text="leet code", brokenLetters="e"))

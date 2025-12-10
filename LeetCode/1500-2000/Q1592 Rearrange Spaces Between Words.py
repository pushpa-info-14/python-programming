class Solution:
    def reorderSpaces(self, text: str) -> str:
        count = text.count(' ')
        words = text.split()
        n = len(words)
        res = ''
        spaces = 0
        rem = count
        if n > 1:
            spaces = count // (n - 1)
            rem = count % (n - 1)
        for word in words[:-1]:
            res += word + ' ' * spaces
        res += words[-1] + ' ' * rem
        return res


s = Solution()
print(s.reorderSpaces(text="  this   is  a sentence "))
print(s.reorderSpaces(text=" practice   makes   perfect"))
print(s.reorderSpaces(text=" practice   makes   perfect"))
print(s.reorderSpaces(text="a"))
print(s.reorderSpaces(text="  a "))

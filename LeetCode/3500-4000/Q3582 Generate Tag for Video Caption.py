class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return "#"

        tag = words[0].lower()
        for word in words[1:]:
            tag += word[0].upper() + word[1:].lower()

        res = '#'
        for c in tag:
            if c.isalpha():
                res += c
        return res[:100]


s = Solution()
print(s.generateTag(caption="Leetcode daily streak achieved"))
print(s.generateTag(caption="can I Go There"))
print(s.generateTag(caption="   "))
print(s.generateTag(
    caption="hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"))

class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        special_chars = []
        for c in s:
            if c.isalpha():
                letters.append(c)
            else:
                special_chars.append(c)
        letters.reverse()
        special_chars.reverse()
        res = list(s)
        idx1 = 0
        idx2 = 0
        for i in range(len(res)):
            c = res[i]
            if c.isalpha():
                res[i] = letters[idx1]
                idx1 += 1
            else:
                res[i] = special_chars[idx2]
                idx2 += 1
        return "".join(res)


s = Solution()
print(s.reverseByType(s=")ebc#da@f("))
print(s.reverseByType(s="z"))
print(s.reverseByType(s="!@#$%^&*()"))

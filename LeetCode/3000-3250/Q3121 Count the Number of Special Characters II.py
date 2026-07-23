class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        lowercase_last = {}
        uppercase_first = {}
        for i in range(n):
            c = word[i]
            if c.islower():
                lowercase_last[c] = i
            elif c not in uppercase_first:
                uppercase_first[c] = i
        res = 0
        for c in lowercase_last.keys():
            if c.upper() in uppercase_first and lowercase_last[c] < uppercase_first[c.upper()]:
                res += 1
        return res


s = Solution()
print(s.numberOfSpecialChars(word="aaAbcBC"))
print(s.numberOfSpecialChars(word="abc"))
print(s.numberOfSpecialChars(word="abBCab"))

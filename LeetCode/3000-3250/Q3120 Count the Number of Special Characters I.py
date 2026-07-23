class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = set()
        uppercase = set()
        for c in word:
            if c.islower() and c not in lowercase:
                lowercase.add(c)
            elif c not in uppercase:
                uppercase.add(c)
        res = 0
        for c in lowercase:
            if c.upper() in uppercase:
                res += 1
        return res


s = Solution()
print(s.numberOfSpecialChars(word="aaAbcBC"))
print(s.numberOfSpecialChars(word="abc"))
print(s.numberOfSpecialChars(word="abBCab"))

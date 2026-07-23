class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
        return False if count == 0 else True


s = Solution()
print(s.doesAliceWin(s="leetcoder"))
print(s.doesAliceWin(s="bbcd"))

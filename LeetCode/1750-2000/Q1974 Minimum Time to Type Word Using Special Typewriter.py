class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        cur = 0
        for c in word:
            p = ord(c) - ord('a')
            if p == cur:
                res += 1
            else:
                x1 = abs(cur - p)
                x2 = abs(26 - x1)
                cur = p
                res += min(x1, x2) + 1
        return res


s = Solution()
print(s.minTimeToType(word="abc"))
print(s.minTimeToType(word="bza"))
print(s.minTimeToType(word="zjpc"))

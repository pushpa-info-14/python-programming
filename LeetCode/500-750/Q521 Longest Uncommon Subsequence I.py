class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))


s = Solution()
print(s.findLUSlength(a="aba", b="cdc"))
print(s.findLUSlength(a="aaa", b="bbb"))
print(s.findLUSlength(a="aaa", b="aaa"))

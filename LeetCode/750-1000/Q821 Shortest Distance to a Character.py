from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        inf = 10 ** 10
        n = len(s)
        res = [inf] * n
        last = inf
        for i in range(n):
            if s[i] == c:
                last = i
            res[i] = min(res[i], abs(i - last))
        for i in reversed(range(n)):
            if s[i] == c:
                last = i
            res[i] = min(res[i], abs(i - last))
        return res


s = Solution()
print(s.shortestToChar(s="loveleetcode", c="e"))
print(s.shortestToChar(s="aaab", c="b"))

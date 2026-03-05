from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for l in range(n):
            counter = defaultdict(int)
            for r in range(l, n):
                counter[s[r]] += 1
                if len(set(counter.values())) == 1:
                    res = max(res, r - l + 1)
        return res


s = Solution()
print(s.longestBalanced(s="abbac"))
print(s.longestBalanced(s="zzabccy"))
print(s.longestBalanced(s="aba"))

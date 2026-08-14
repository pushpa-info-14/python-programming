from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        counter = defaultdict(int)
        res = 0
        l = 0
        for r in range(n):
            counter[s[r]] += 1
            while counter[s[r]] > 2 and l < r:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


s = Solution()
print(s.maximumLengthSubstring(s="bcbbbcba"))
print(s.maximumLengthSubstring(s="aaaa"))

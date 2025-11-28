from collections import defaultdict


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        counter = defaultdict(int)
        l = 0
        for r in range(n):
            counter[s[r]] += 1
            if r - l + 1 == 3:
                if len(counter.keys()) == 3:
                    res += 1
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
        return res


s = Solution()
print(s.countGoodSubstrings(s="xyzzaz"))
print(s.countGoodSubstrings(s="aababcabc"))

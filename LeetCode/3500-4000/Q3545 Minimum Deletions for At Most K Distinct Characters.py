from collections import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = Counter(s)
        counts = sorted(counter.values())
        res = 0
        for i in range(len(counts) - k):
            res += counts[i]
        return res


s = Solution()
print(s.minDeletion(s="abc", k=2))
print(s.minDeletion(s="aabb", k=2))
print(s.minDeletion(s="yyyzz", k=1))

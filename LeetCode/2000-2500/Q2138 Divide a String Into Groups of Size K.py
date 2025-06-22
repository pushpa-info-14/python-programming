from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []

        if len(s) % k:
            s += ((k - (len(s) % k)) * fill)

        for i in range(k, len(s) + 1, k):
            res.append(s[i - k:i])
        return res


s = Solution()
print(s.divideString(s="abcdefghi", k=3, fill="x"))
print(s.divideString(s="abcdefghij", k=3, fill="x"))

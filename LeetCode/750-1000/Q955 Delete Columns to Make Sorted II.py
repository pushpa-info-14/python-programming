from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        words = [""] * n
        res = 0
        for c in range(m):
            is_sorted = True
            for r in range(1, n):
                if words[r - 1] + strs[r - 1][c] > words[r] + strs[r][c]:
                    is_sorted = False
                    break
            if is_sorted:
                for r in range(n):
                    words[r] += strs[r][c]
            else:
                res += 1
        return res


s = Solution()
print(s.minDeletionSize(strs=["ca", "bb", "ac"]))
print(s.minDeletionSize(strs=["xc", "yb", "za"]))
print(s.minDeletionSize(strs=["zyx", "wvu", "tsr"]))
print(s.minDeletionSize(strs=["xga", "xfb", "yfa"]))

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        n = len(strs)
        m = len(strs[0])
        for c in range(m):
            for r in range(1, n):
                if strs[r - 1][c] > strs[r][c]:
                    res += 1
                    break
        return res


s = Solution()
print(s.minDeletionSize(strs=["cba", "daf", "ghi"]))
print(s.minDeletionSize(strs=["a", "b"]))
print(s.minDeletionSize(strs=["zyx", "wvu", "tsr"]))

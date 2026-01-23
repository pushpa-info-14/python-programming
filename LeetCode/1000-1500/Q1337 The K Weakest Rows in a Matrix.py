from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        scores = []
        m = len(mat)
        for i in range(m):
            ones = mat[i].count(1)
            scores.append([ones, i])
        scores.sort()

        res = []
        for i in range(k):
            res.append(scores[i][1])
        return res


s = Solution()
print(s.kWeakestRows(mat=[[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], k=3))
print(s.kWeakestRows(mat=[[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], k=2))

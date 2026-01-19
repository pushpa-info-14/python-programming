from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                pre_sum[r][c] = (
                        mat[r - 1][c - 1]
                        + pre_sum[r - 1][c]
                        + pre_sum[r][c - 1]
                        - pre_sum[r - 1][c - 1]
                )
        res = 0
        for r in range(m):
            for c in range(n):
                for k in range(min(m - r, n - c)):
                    cur = (
                            pre_sum[r + k + 1][c + k + 1]
                            + pre_sum[r][c]
                            - pre_sum[r][c + k + 1]
                            - pre_sum[r + k + 1][c]
                    )
                    if cur <= threshold:
                        res = max(res, k + 1)
                    else:
                        break
        return res

    def maxSideLength2(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                pre_sum[r][c] = (
                        mat[r - 1][c - 1]
                        + pre_sum[r - 1][c]
                        + pre_sum[r][c - 1]
                        - pre_sum[r - 1][c - 1]
                )
        res = 0
        for r in range(m):
            for c in range(n):
                for k in range(res, min(m - r, n - c)):
                    cur = (
                            pre_sum[r + k + 1][c + k + 1]
                            + pre_sum[r][c]
                            - pre_sum[r][c + k + 1]
                            - pre_sum[r + k + 1][c]
                    )
                    if cur <= threshold:
                        res = k + 1
                    else:
                        break
        return res


s = Solution()
print(s.maxSideLength(mat=[[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], threshold=4))
print(s.maxSideLength(mat=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]],
                      threshold=1))
print(s.maxSideLength(mat=[[0]], threshold=0))
print("------------------------")
print(s.maxSideLength2(mat=[[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], threshold=4))
print(s.maxSideLength2(mat=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]],
                      threshold=1))
print(s.maxSideLength2(mat=[[0]], threshold=0))

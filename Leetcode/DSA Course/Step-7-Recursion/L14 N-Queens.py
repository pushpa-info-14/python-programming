from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [["."] * n for _ in range(n)]
        pos_diagonal = set()
        neg_diagonal = set()
        column = set()

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in column or (r + c) in pos_diagonal or (r - c) in neg_diagonal:
                    continue
                board[r][c] = "Q"
                pos_diagonal.add(r + c)
                neg_diagonal.add(r - c)
                column.add(c)
                dfs(r + 1)
                board[r][c] = "."
                pos_diagonal.remove(r + c)
                neg_diagonal.remove(r - c)
                column.remove(c)

        dfs(0)
        return res


s = Solution()
print(s.solveNQueens(4))

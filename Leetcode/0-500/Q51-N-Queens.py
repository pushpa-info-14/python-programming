from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = set()
        positive_diagonal = set()  # r + c
        negative_diagonal = set()  # r - c
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in column or r + c in positive_diagonal or r - c in negative_diagonal:
                    continue

                column.add(c)
                positive_diagonal.add(r + c)
                negative_diagonal.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                column.remove(c)
                positive_diagonal.remove(r + c)
                negative_diagonal.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

s = Solution()
print(s.solveNQueens(4))
print(s.solveNQueens(1))
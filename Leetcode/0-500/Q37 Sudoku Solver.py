from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(row, col, digit):
            for i in range(9):
                if board[row][i] == digit:
                    return False
                if board[i][col] == digit:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == digit:
                    return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for d in "123456789":
                            if valid(r, c, d):
                                board[r][c] = d
                                if solve():
                                    return True
                                else:
                                    board[r][c] = "."
                        return False
            return True

        solve()

        print(board)

    def solveSudoku2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[(i // 3, j // 3)].add(board[i][j])

        def solve(row):
            for r in range(row, 9):
                for c in range(9):
                    if board[r][c] != ".":
                        continue

                    for d in "123456789":
                        if (d not in rows[r] and
                                d not in cols[c] and
                                d not in squares[(r // 3, c // 3)]):
                            board[r][c] = d
                            rows[r].add(d)
                            cols[c].add(d)
                            squares[(r // 3, c // 3)].add(d)
                            if solve(r):
                                return True
                            else:
                                board[r][c] = "."
                                rows[r].remove(d)
                                cols[c].remove(d)
                                squares[(r // 3, c // 3)].remove(d)
                    return False
            return True

        solve(0)

        print(board)

    def solveSudoku3(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[(i // 3, j // 3)].add(board[i][j])

        def solve(r, c):
            if r == 9:
                return True
            next_r = r + (c + 1) // 9
            next_c = (c + 1) % 9

            if board[r][c] != ".":
                return solve(next_r, next_c)
            else:
                for d in "123456789":
                    if (d not in rows[r] and
                            d not in cols[c] and
                            d not in squares[(r // 3, c // 3)]):
                        board[r][c] = d
                        rows[r].add(d)
                        cols[c].add(d)
                        squares[(r // 3, c // 3)].add(d)
                        if solve(next_r, next_c):
                            return True
                        else:
                            board[r][c] = "."
                            rows[r].remove(d)
                            cols[c].remove(d)
                            squares[(r // 3, c // 3)].remove(d)
            return False

        solve(0, 0)

        print(board)


s = Solution()
s.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
s.solveSudoku2([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
s.solveSudoku3([[".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", "9", ".", ".", "1", ".", ".", "3", "."],
                [".", ".", "6", ".", "2", ".", "7", ".", "."],
                [".", ".", ".", "3", ".", "4", ".", ".", "."],
                ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", "2", "5", ".", "6", "4", ".", "."],
                [".", "8", ".", ".", ".", ".", ".", "1", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."]])

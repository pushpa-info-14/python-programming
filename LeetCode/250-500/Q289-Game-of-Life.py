from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        board_copy = [[0] * n for i in range(m)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        for i in range(m):
            for j in range(n):
                board_copy[i][j] = board[i][j]

        for r in range(m):
            for c in range(n):
                nei_count = 0
                for dir in range(8):
                    nr = r + directions[dir][0]
                    nc = c + directions[dir][1]
                    if nr < 0 or nc < 0 or nr == m or nc == n:
                        continue
                    if board_copy[nr][nc]:
                        nei_count += 1
                if board_copy[r][c]:
                    if nei_count < 2:
                        board[r][c] = 0
                    elif nei_count > 3:
                        board[r][c] = 0
                else:
                    if nei_count == 3:
                        board[r][c] = 1

        print(board_copy)
        print(board)


s = Solution()
print(s.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
print(s.gameOfLife([[1, 1], [1, 0]]))

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[0] * n for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            visited[r][c] = 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc] or board[nr][nc] == 'X':
                    continue
                dfs(nr, nc)

        for row in range(m):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][n - 1] == "O":
                dfs(row, n - 1)
        for col in range(n):
            if board[0][col] == "O":
                dfs(0, col)
            if board[m - 1][col] == "O":
                dfs(m - 1, col)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"

        print(board)


# LeetCode 130
s = Solution()
s.solve(board=[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
s.solve(board=[["X"]])

from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10 ** 9 + 7
        m = len(board)
        n = len(board[0])
        directions = [[0, 1], [1, 0], [1, 1]]
        visited = {(0, 0)}

        @cache
        def dfs(r, c):
            if (r, c) == (m - 1, n - 1):
                return 0, 1  # weight, number of paths
            cur = 0
            if board[r][c].isnumeric():
                cur += int(board[r][c])
            freq = defaultdict(int)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n or board[nr][nc] == 'X' or (nr, nc) in visited:
                    continue
                w, count = dfs(nr, nc)
                if count:
                    freq[w] += count
            if len(freq) == 0:
                return 0, 0
            mx = max(freq)
            mx_freq = freq[mx] % mod
            return mx + cur, mx_freq

        res = dfs(0, 0)
        return [res[0], res[1]]


s = Solution()
print(s.pathsWithMaxScore(board=["E23", "2X2", "12S"]))
print(s.pathsWithMaxScore(board=["E12", "1X1", "21S"]))
print(s.pathsWithMaxScore(board=["E11", "XXX", "11S"]))

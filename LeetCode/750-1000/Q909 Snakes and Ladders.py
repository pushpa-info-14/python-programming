from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        is_odd = True
        edges = []
        for r in range(n - 1, -1, -1):
            for c in range(n):
                if is_odd:
                    edges.append(board[r][c])
                else:
                    edges.append(board[r][n - 1 - c])
            is_odd = not is_odd

        inf = 10 ** 9
        length = len(edges)
        distance = [inf] * length
        distance[0] = 0
        q = deque()
        q.append((0, 0))

        while q:
            dist, node = q.popleft()

            for i in range(1, 7):
                nei = node + i
                if nei >= length:
                    continue
                if edges[nei] != -1:
                    nei = edges[nei] - 1  # Zero based indexing

                if distance[nei] > dist + 1:
                    distance[nei] = dist + 1
                    q.append((dist + 1, nei))

        res = distance[-1]
        if res != inf:
            return res
        return -1


s = Solution()
print(s.snakesAndLadders(
    board=[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
           [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]))
print(s.snakesAndLadders(board=[[-1, -1], [-1, 3]]))
print(s.snakesAndLadders(board=[[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]]))
print(s.snakesAndLadders(board=[[-1, -1], [-1, 1]]))

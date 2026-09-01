from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ids = [[0] * n for _ in range(m)]
        l_count = 0
        q = deque()
        sr, sc = 0, 0
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    ids[r][c] = 1 << l_count
                    l_count += 1
        full = 1 << l_count
        best_energy = [[[-1 for _ in range(full)] for _ in range(n)] for _ in range(m)]
        q.append((sr, sc, 0, energy, 0))  # r, c, mask, e, steps
        best_energy[sr][sc][0] = energy
        while q:
            r, c, mask, e, steps = q.popleft()
            if mask == full - 1:
                return steps
            if e == 0:
                continue
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n or classroom[nr][nc] == 'X':
                    continue
                ne = energy if classroom[nr][nc] == 'R' else e - 1
                n_mask = mask | ids[nr][nc]
                if ne > best_energy[nr][nc][n_mask]:
                    best_energy[nr][nc][n_mask] = ne
                    q.append((nr, nc, n_mask, ne, steps + 1))

        return -1


s = Solution()
print(s.minMoves(classroom=["S.", "XL"], energy=2))
print(s.minMoves(classroom=["LS", "RL"], energy=4))
print(s.minMoves(classroom=["L.S", "RXL"], energy=3))

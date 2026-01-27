from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[False] * n for _ in range(m)]
        res = [image[r].copy() for r in range(m)]

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c, initial_color):
            visited[r][c] = True
            res[r][c] = color
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc] or image[nr][nc] != initial_color:
                    continue
                dfs(nr, nc, initial_color)

        dfs(sr, sc, image[sr][sc])
        return res


# LeetCode 733
s = Solution()
print(s.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
print(s.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0))

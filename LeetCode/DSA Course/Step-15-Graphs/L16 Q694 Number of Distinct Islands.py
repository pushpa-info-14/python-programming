from typing import List


class Solution:
    def distinctIslands(self, arr: List[List[int]]) -> int:
        n = len(arr)
        m = len(arr[0])
        visited = [[0] * m for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        island_map = {}

        def dfs(r, c, index):
            visited[r][c] = 1
            island_map[count].append((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == n or nc < 0 or nc == m or visited[nr][nc] or arr[nr][nc] == 0:
                    continue
                dfs(nr, nc, index)

        count = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and arr[i][j] == 1:
                    island_map[count] = []
                    dfs(i, j, count)
                    count += 1

        unique = set()
        for key in island_map.keys():
            island = island_map[key]
            island.sort()
            min_r = island[0][0]
            min_c = island[0][1]
            for i in range(len(island)):
                island[i] = (island[i][0] - min_r, island[i][1] - min_c)
            unique.add(tuple(island))

        return len(unique)


s = Solution()
print(s.distinctIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))  # 1
print(s.distinctIslands([[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]))  # 3

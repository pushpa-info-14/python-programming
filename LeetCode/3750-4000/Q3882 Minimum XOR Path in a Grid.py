class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[False] * 1024 for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = True
        for i in range(m):
            for j in range(n):
                for k in range(1024):
                    if i > 0 and dp[i - 1][j][k]:
                        dp[i][j][k ^ grid[i][j]] = True
                    if j > 0 and dp[i][j - 1][k]:
                        dp[i][j][k ^ grid[i][j]] = True
        for k in range(1024):
            if dp[m - 1][n - 1][k]:
                return k
        return -1


s = Solution()
print(s.minCost(grid=[[1, 2], [3, 4]]))
print(s.minCost(grid=[[6, 7], [5, 8]]))
print(s.minCost(grid=[[2, 7, 5]]))

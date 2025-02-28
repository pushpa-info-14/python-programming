class Solution:
    def gridUniquePaths1(self, m: int, n: int) -> int:
        def dfs(i, j):
            if i == 0 and j == 0: return 1
            if i < 0 or j < 0: return 0
            up = dfs(i - 1, j)
            left = dfs(i, j - 1)
            return up + left

        return dfs(m - 1, n - 1)

    def gridUniquePaths2(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i == 0 and j == 0: return 1
            if i < 0 or j < 0: return 0

            if dp[i][j] != -1:
                return dp[i][j]

            up = dfs(i - 1, j)
            left = dfs(i, j - 1)
            dp[i][j] = up + left
            return dp[i][j]

        return dfs(m - 1, n - 1)

    def gridUniquePaths3(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                dp[r][c] += dp[r - 1][c] + dp[r][c - 1]
        return dp[m][n]

    def gridUniquePaths4(self, m: int, n: int) -> int:
        prev = [0] * n

        for r in range(m):
            cur = [0] * n
            for c in range(n):
                if r == 0 and c == 0:
                    cur[0] = 1
                else:
                    if r > 0: cur[c] += prev[c]
                    if c > 0: cur[c] += cur[c - 1]
            prev = cur.copy()
        return prev[n - 1]


s = Solution()
print(s.gridUniquePaths1(2, 2))
print(s.gridUniquePaths1(3, 3))
print(s.gridUniquePaths1(4, 4))

print(s.gridUniquePaths2(2, 2))
print(s.gridUniquePaths2(3, 3))
print(s.gridUniquePaths2(4, 4))

print(s.gridUniquePaths3(2, 2))
print(s.gridUniquePaths3(3, 3))
print(s.gridUniquePaths3(4, 4))

print(s.gridUniquePaths4(2, 2))
print(s.gridUniquePaths4(3, 3))
print(s.gridUniquePaths4(4, 4))

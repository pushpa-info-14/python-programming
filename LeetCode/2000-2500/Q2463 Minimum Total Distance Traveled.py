from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        inf = 10 ** 20
        factory.sort()
        robot.sort()
        slots = []
        for pos, limit in factory:
            slots += [pos] * limit
        m = len(robot)
        n = len(slots)
        memo = [[None] * (n + 1) for _ in range(m + 1)]

        def dfs(i, j):
            if i == m:
                memo[i][j] = 0
                return 0
            if j == n:
                memo[i][j] = inf
                return inf
            if memo[i][j]:
                return memo[i][j]
            cur = inf
            # not take
            cur = min(cur, dfs(i, j + 1))
            # take
            d = abs(slots[j] - robot[i])
            cur = min(cur, d + dfs(i + 1, j + 1))
            memo[i][j] = cur
            return cur

        return dfs(0, 0)

    def minimumTotalDistance2(self, robot: List[int], factory: List[List[int]]) -> int:
        inf = 10 ** 20
        factory.sort()
        robot.sort()
        slots = []
        for pos, limit in factory:
            slots += [pos] * limit
        m = len(robot)
        n = len(slots)
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[m][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                d = abs(slots[j] - robot[i])
                dp[i][j] = min(dp[i][j], dp[i][j + 1], d + dp[i + 1][j + 1])

        return dp[0][0]


s = Solution()
print(s.minimumTotalDistance(robot=[0, 4, 6], factory=[[2, 2], [6, 2]]))
print(s.minimumTotalDistance(robot=[1, -1], factory=[[-2, 1], [2, 1]]))
print("--------------")
print(s.minimumTotalDistance2(robot=[0, 4, 6], factory=[[2, 2], [6, 2]]))
print(s.minimumTotalDistance2(robot=[1, -1], factory=[[-2, 1], [2, 1]]))

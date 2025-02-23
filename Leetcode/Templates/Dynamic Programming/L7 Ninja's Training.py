"""
    t0  t1  t2
D1  10  50  1
D2  5   100 11
"""
from typing import List


class Solution:
    def ninjaTraining(self, n: int, points: List[List[int]]) -> int:
        dp = [[-1] * 4 for _ in range(n)]

        def dfs(day, last):
            if day == 0:
                cur_max = 0
                for i in range(3):
                    if i != last:
                        cur_max = max(cur_max, points[0][i])
                return cur_max

            if dp[day][last] != -1:
                return dp[day][last]

            cur_max = 0
            for i in range(3):
                if i != last:
                    point = dfs(day - 1, i) + points[day][i]
                    cur_max = max(cur_max, point)
            dp[day][last] = cur_max
            return dp[day][last]

        return dfs(n - 1, 3)

    def ninjaTrainingTabulation(self, n: int, points: List[List[int]]) -> int:
        dp = [[-1] * 4 for _ in range(n)]

        for task in range(3):
            dp[0][task] = points[0][task]

        for day in range(1, n):
            for last_task in range(3):
                for next_task in range(3):
                    if last_task != next_task:
                        dp[day][next_task] = max(dp[day][next_task], dp[day - 1][last_task] + points[day][next_task])

        ans = 0
        for i in range(3):
            ans = max(ans, dp[n - 1][i])
        return ans

    def ninjaTrainingTabulation2(self, n: int, points: List[List[int]]) -> int:
        prev = [0] * 3

        for task in range(3):
            prev[task] = points[0][task]

        for day in range(1, n):
            cur = [0] * 3
            for last_task in range(3):
                for next_task in range(3):
                    if last_task != next_task:
                        cur[next_task] = max(cur[next_task], prev[last_task] + points[day][next_task])
            prev = cur.copy()

        ans = 0
        for i in range(3):
            ans = max(ans, prev[i])
        return ans


s = Solution()
print(s.ninjaTraining(2, [[10, 50, 1], [5, 100, 11]]))
print(s.ninjaTrainingTabulation(2, [[10, 50, 1], [5, 100, 11]]))
print(s.ninjaTrainingTabulation2(2, [[10, 50, 1], [5, 100, 11]]))

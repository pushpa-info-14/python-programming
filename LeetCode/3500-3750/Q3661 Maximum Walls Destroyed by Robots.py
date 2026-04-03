import bisect
from typing import List


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        inf = 10 ** 10
        n = len(robots)
        walls.sort()

        def count(l, r):
            if l > r: return 0
            return bisect.bisect_right(walls, r) - bisect.bisect_left(walls, l)

        arr = []
        for i in range(n):
            arr.append([robots[i], distance[i]])
        arr.sort()
        arr.append([inf, 0])  # Sentinel

        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = count(arr[0][0] - arr[0][1], arr[0][0] - 1)

        for i in range(n):
            l, ld = arr[i]
            r, rd = arr[i + 1]
            left1, right1 = l + 1, min(l + ld, r - 1)
            left2, right2 = max(l + 1, r - rd), r - 1
            left_count = count(left1, right1)
            right_count = count(left2, right2)
            both_count = left_count + right_count - count(max(left1, left2), min(right1, right2))

            dp[i + 1][0] = max(
                dp[i][0] + left_count,  # Left shoots right
                dp[i][1]  # Nothing
            )
            dp[i + 1][1] = max(
                dp[i][1] + right_count,  # Right shoots left
                dp[i][0] + both_count  # Both shoot
            )

        res = dp[-1][1]
        for pos in robots:
            res += count(pos, pos)
        return res


s = Solution()
print(s.maxWalls(robots=[4], distance=[3], walls=[1, 10]))
print(s.maxWalls(robots=[10, 2], distance=[5, 1], walls=[5, 2, 7]))
print(s.maxWalls(robots=[1, 2], distance=[100, 1], walls=[10]))

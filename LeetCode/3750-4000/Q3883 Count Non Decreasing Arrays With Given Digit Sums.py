import bisect
from collections import defaultdict


class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        n = len(digitSum)
        mod = 10 ** 9 + 7
        mp = defaultdict(list)
        for i in range(5001):
            x = i
            cur = 0
            while x:
                cur += x % 10
                x //= 10
            mp[cur].append(i)
        dp = [defaultdict(int) for _ in range(n)]
        for x in mp[digitSum[0]]:
            dp[0][x] = 1
        for i in range(1, n):
            v1 = mp[digitSum[i - 1]]
            m = len(v1)
            if m > 0:
                pre_sum = [0] * m
                pre_sum[0] = dp[i - 1][v1[0]]
                for j in range(1, m):
                    pre_sum[j] = (pre_sum[j - 1] + dp[i - 1][v1[j]]) % mod

                v2 = mp[digitSum[i]]
                for x in v2:
                    idx = bisect.bisect_right(v1, x) - 1
                    if idx >= 0:
                        dp[i][x] += pre_sum[idx]
                        dp[i][x] %= mod
        res = 0
        for x in mp[digitSum[-1]]:
            res = (res + dp[n - 1][x]) % mod

        return res


s = Solution()
print(s.countArrays(digitSum=[25, 1]))
print(s.countArrays(digitSum=[1]))
print(s.countArrays(digitSum=[2, 49, 23]))

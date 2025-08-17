class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        sm = 1.0
        for i in range(1, n + 1):
            dp[i] = sm / maxPts
            if i < k:
                sm += dp[i]
            if i >= maxPts:
                sm -= dp[i - maxPts]
        res = sum(dp[k:])
        return res


s = Solution()
print(s.new21Game(n=10, k=1, maxPts=10))
print(s.new21Game(n=6, k=1, maxPts=10))
print(s.new21Game(n=21, k=17, maxPts=10))

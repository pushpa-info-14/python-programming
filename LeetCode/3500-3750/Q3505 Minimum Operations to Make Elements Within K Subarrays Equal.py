from typing import List

from sortedcontainers import SortedList


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        l = SortedList()
        h = SortedList()
        ls, hs = 0, 0
        vals = [0] * n

        for i in range(n):
            if not h or h[0][0] <= nums[i]:
                h.add([nums[i], i])
                hs += nums[i]
            else:
                l.add([nums[i], i])
                ls += nums[i]
            if i >= x:
                val = nums[i - x]
                if [val, i - x] in l:
                    l.discard([val, i - x])
                    ls -= val
                else:
                    h.discard([val, i - x])
                    hs -= val
            while len(l) + 1 < len(h):
                val, idx = h.pop(0)
                hs -= val
                l.add([val, idx])
                ls += val
            while len(l) > len(h):
                val, idx = l.pop(-1)
                ls -= val
                h.add([val, idx])
                hs += val
            if i >= x - 1:
                vals[i] = (len(l) * h[0][0] - ls) + (hs - len(h) * h[0][0])

        inf = 10 ** 20
        dp = [[inf] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0
        dp[x - 1][1] = vals[x - 1]
        for i in range(x, n):
            for j in range(1, k + 1):
                dp[i][j] = min(dp[i - 1][j], vals[i] + dp[i - x][j - 1])
        return dp[-1][-1]


s = Solution()
print(s.minOperations(nums=[5, -2, 1, 3, 7, 3, 6, 4, -1], x=3, k=2))
print(s.minOperations(nums=[9, -2, -2, -2, 1, 5], x=2, k=2))

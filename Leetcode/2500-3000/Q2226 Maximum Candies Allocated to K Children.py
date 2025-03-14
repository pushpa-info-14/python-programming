from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0

        res = 0
        l, r = 1, total // k
        while l <= r:
            m = (l + r) // 2
            cnt = 0
            for c in candies:
                if c >= m:
                    cnt += c // m
                if cnt >= k:
                    break
            if cnt >= k:
                res = m
                l = m + 1
            else:
                r = m - 1

        return res


s = Solution()
print(s.maximumCandies([5, 8, 6], 3))
print(s.maximumCandies([1, 2, 3, 4, 10], 5))

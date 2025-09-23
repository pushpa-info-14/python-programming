import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        cnt = 0
        while cnt < n:
            rows += 1
            cnt += rows

        if cnt == n:
            return rows
        else:
            return rows - 1

    def arrangeCoins2(self, n: int) -> int:

        # x(x+1)/2 = n
        return int(math.sqrt(2 * n + 0.25) - 0.5)

    def arrangeCoins3(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            coins = (mid + 1) * mid // 2
            if coins == n:
                return mid
            elif coins < n:
                l = mid + 1
            else:
                r = mid - 1
        return r


s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
print(s.arrangeCoins(1))
print(s.arrangeCoins2(5))
print(s.arrangeCoins2(8))
print(s.arrangeCoins2(1))
print(s.arrangeCoins3(5))
print(s.arrangeCoins3(8))
print(s.arrangeCoins3(1))

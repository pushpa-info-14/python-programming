class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            power = mid * mid
            if power == x:
                return mid
            elif power < x:
                l = mid + 1
            else:
                r = mid - 1
        return r


s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))
print(s.mySqrt(10))
print(s.mySqrt(17))

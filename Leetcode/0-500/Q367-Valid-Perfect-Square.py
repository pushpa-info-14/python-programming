class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l, r = 0, num
        while l < r:
            mid = l + (r - l + 1) // 2
            power = mid * mid

            if power == num:
                return True
            elif power < num:
                l = mid
            else:
                r = mid - 1
        return False


s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(9))
print(s.isPerfectSquare(14))

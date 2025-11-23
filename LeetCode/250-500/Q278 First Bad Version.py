# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return True if version == 15 else False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


s = Solution()
print(s.firstBadVersion(20))

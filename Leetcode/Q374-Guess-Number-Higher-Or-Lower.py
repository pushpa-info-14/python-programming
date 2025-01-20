# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num > 6:
        return -1
    elif num < 6:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = l + (r - l + 1) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                r = mid - 1
            else:
                l = mid + 1


s = Solution()
print(s.guessNumber(10))

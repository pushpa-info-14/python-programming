from typing import List


def isNoZero(num):
    while num:
        digit = num % 10
        if digit == 0:
            return False
        num //= 10
    return True


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            a = i
            b = n - i

            if isNoZero(a) and isNoZero(b):
                return [a, b]
        return []


s = Solution()
print(s.getNoZeroIntegers(2))
print(s.getNoZeroIntegers(11))

import math


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        k = int(math.log2(n))
        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(2 ** k ^ n)


s = Solution()
print(s.minimumOneBitOperations(3))
print(s.minimumOneBitOperations(6))
print(s.minimumOneBitOperations(4))

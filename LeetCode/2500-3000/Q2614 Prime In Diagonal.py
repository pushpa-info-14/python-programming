import math
from typing import List


def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        candidates = set()
        n = len(nums)
        for r in range(n):
            candidates.add(nums[r][r])
            candidates.add(nums[r][n - r - 1])
        for num in sorted(candidates, reverse=True):
            if is_prime(num):
                return num
        return 0


s = Solution()
print(s.diagonalPrime(nums=[[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
print(s.diagonalPrime(nums=[[1, 2, 3], [5, 17, 7], [9, 11, 10]]))

from functools import cache
from typing import List


@cache
def gcd(a, b):  # Euclidean Algorithm
    while b:
        a, b = b, a % b
    return abs(a)


@cache
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        res = []
        curr = nums[0]
        for num in nums[1:]:
            if gcd(curr, num) > 1:
                curr = lcm(curr, num)
                while res and gcd(curr, res[-1]) > 1:
                    curr = lcm(curr, res.pop())
            else:
                res.append(curr)
                curr = num
        res.append(curr)
        return res


s = Solution()
print(s.replaceNonCoprimes(nums=[6, 4, 3, 2, 7, 6, 2]))
print(s.replaceNonCoprimes(nums=[2, 2, 1, 1, 3, 3, 3]))
print(s.replaceNonCoprimes(nums=[48757]))
print(s.replaceNonCoprimes(nums=[517, 11, 121, 517, 3, 51, 3, 1887, 5]))  # [5687,1887,5]
print(s.replaceNonCoprimes(
    nums=[2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2,
          3, 2, 3, 2, 3, 2, 3, 6, 6]))

from typing import List


def gcd(a, b):
    while a and b:
        a, b = b, a % b
    return a


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return gcd(nums[0], nums[-1])


s = Solution()
print(s.findGCD(nums=[2, 5, 6, 9, 10]))
print(s.findGCD(nums=[7, 5, 6, 8, 3]))
print(s.findGCD(nums=[3, 3]))

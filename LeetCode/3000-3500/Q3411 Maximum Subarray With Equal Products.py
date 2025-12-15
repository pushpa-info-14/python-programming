from typing import List


def gcd(a, b):
    while a and b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            cur_prod = nums[i]
            cur_gcd = nums[i]
            cur_lcm = nums[i]
            for j in range(i + 1, n):
                cur_prod *= nums[j]
                cur_gcd = gcd(cur_gcd, nums[j])
                cur_lcm = lcm(cur_lcm, nums[j])
                if cur_prod == cur_lcm * cur_gcd:
                    res = max(res, j - i + 1)
        return res


# LCM(a, b) = |a × b| / GCD(a, b)
s = Solution()
print(s.maxLength(nums=[1, 2, 1, 2, 1, 1, 1]))
print(s.maxLength(nums=[2, 3, 4, 5, 6]))
print(s.maxLength(nums=[1, 2, 3, 1, 4, 5, 1]))

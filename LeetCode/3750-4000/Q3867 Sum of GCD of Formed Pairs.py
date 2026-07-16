from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        mx = 0
        for num in nums:
            mx = max(mx, num)
            prefix_gcd.append(gcd(num, mx))
        prefix_gcd.sort()
        res = 0
        l, r = 0, len(prefix_gcd) - 1
        while l < r:
            num1 = prefix_gcd[l]
            num2 = prefix_gcd[r]
            res += gcd(num1, num2)
            l += 1
            r -= 1
        return res


s = Solution()
print(s.gcdSum(nums=[2, 6, 4]))
print(s.gcdSum(nums=[3, 6, 2, 8]))

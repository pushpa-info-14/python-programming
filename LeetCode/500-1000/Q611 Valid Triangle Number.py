from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(x for x in nums if x > 0)
        n = len(nums)
        res = 0
        for i in range(n):
            a = nums[i]
            k = 0
            for j in range(i + 1, n):
                b = nums[j]
                while k < n and a + b > nums[k]:
                    k += 1
                res += (k - 1) - (j + 1) + 1
        return res


s = Solution()
print(s.triangleNumber(nums=[2, 2, 3, 4]))
print(s.triangleNumber(nums=[4, 2, 3, 4]))
print(s.triangleNumber(nums=[0, 0, 0]))

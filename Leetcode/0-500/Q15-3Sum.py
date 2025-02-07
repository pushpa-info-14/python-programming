from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0, 1, 1]))
print(s.threeSum([0, 0, 0]))
print(s.threeSum([0, 0, 0, 0]))

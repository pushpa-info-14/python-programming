from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        zeros = 0
        ones = 0
        l = 0
        res = 0
        for r in range(n):
            if nums[r]:
                ones += 1
            else:
                zeros += 1
            while zeros > 1:
                if nums[l]:
                    ones -= 1
                else:
                    zeros -= 1
                l += 1
            res = max(res, ones)
        res = max(res, ones)
        return res if res != n else n - 1


s = Solution()
print(s.longestSubarray(nums=[1, 1, 0, 1]))  # 3
print(s.longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
print(s.longestSubarray(nums=[1, 1, 1]))  # 2

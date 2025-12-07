from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        res = 0
        r = 0
        while r < n:
            if nums[r] % 2 == 0 and nums[r] <= threshold:
                l = r
                while (r + 1 < n and nums[r] <= threshold
                       and nums[r + 1] <= threshold and nums[r] % 2 != nums[r + 1] % 2):
                    r += 1
                res = max(res, r - l + 1)
            r += 1
        return res


s = Solution()
print(s.longestAlternatingSubarray(nums=[3, 2, 5, 4], threshold=5))
print(s.longestAlternatingSubarray(nums=[1, 2], threshold=2))
print(s.longestAlternatingSubarray(nums=[2, 3, 4, 5], threshold=4))
print(s.longestAlternatingSubarray(nums=[4], threshold=1))
print(s.longestAlternatingSubarray(nums=[4, 10, 3], threshold=10))

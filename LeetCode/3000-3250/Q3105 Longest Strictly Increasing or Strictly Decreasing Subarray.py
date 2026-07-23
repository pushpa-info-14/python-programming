from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        counter = 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                counter += 1
                res = max(res, counter)
            else:
                counter = 1
        counter = 1
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                counter += 1
                res = max(res, counter)
            else:
                counter = 1
        return res


s = Solution()
print(s.longestMonotonicSubarray([1, 4, 3, 3, 2]))
print(s.longestMonotonicSubarray([3, 3, 3]))

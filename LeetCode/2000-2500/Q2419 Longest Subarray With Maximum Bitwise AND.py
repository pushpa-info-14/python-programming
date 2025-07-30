from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = max(nums)
        res = 0
        count = 0
        for i in range(n):
            if nums[i] == max_value:
                count += 1
            else:
                res = max(res, count)
                count = 0
        res = max(res, count)
        return res


# Max consecutive count of max_value number
s = Solution()
print(s.longestSubarray(nums=[1, 2, 3, 3, 2, 2]))
print(s.longestSubarray(nums=[1, 2, 3, 4]))

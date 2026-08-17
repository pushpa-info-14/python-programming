from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        zeros = 0
        for num in nums:
            res ^= num
            if num == 0:
                zeros += 1

        if zeros == n:
            return 0

        if res != 0:
            return len(nums)
        else:
            return len(nums) - 1


s = Solution()
print(s.longestSubsequence(nums=[1, 2, 3]))
print(s.longestSubsequence(nums=[2, 3, 4]))

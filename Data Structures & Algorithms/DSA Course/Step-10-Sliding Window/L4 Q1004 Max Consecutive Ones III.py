from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        max_len = 0
        zeros = 0
        while r < n:
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                while zeros > k:
                    if nums[l] == 0:
                        zeros -= 1
                    l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))

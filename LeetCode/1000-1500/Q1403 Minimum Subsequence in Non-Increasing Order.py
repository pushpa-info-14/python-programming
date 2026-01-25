from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        res = []
        right = sum(nums)
        left = 0
        for num in nums:
            left += num
            right -= num
            res.append(num)
            if left > right:
                break
        return res


s = Solution()
print(s.minSubsequence(nums=[4, 3, 10, 9, 8]))
print(s.minSubsequence(nums=[4, 4, 7, 6, 7]))

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_index = 0
        for i in range(n):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
        return True


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))

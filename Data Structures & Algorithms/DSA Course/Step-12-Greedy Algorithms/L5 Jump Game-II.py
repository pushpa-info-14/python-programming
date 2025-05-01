from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        l, r = 0, 0

        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            jumps += 1
            l = r + 1
            r = farthest
        return jumps


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([2, 3, 0, 1, 4]))

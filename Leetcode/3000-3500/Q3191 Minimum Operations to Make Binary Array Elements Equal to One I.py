from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                res += 1
        if not nums[-1] or not nums[-2]:
            return -1
        return res


s = Solution()
print(s.minOperations([0, 1, 1, 1, 0, 0]))

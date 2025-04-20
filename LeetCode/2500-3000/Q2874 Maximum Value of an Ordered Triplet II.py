from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prefix_max = nums[0]
        max_diff = 0

        for k in range(1, n):
            res = max(res, max_diff * nums[k])

            max_diff = max(max_diff, prefix_max - nums[k])
            prefix_max = max(prefix_max, nums[k])

        return res


s = Solution()
print(s.maximumTripletValue([12, 6, 1, 2, 7]))
print(s.maximumTripletValue([1, 10, 3, 4, 19]))

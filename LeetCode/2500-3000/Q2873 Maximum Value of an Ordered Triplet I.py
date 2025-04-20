from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        left = nums[0]
        for j in range(1, n):
            if nums[j] > left:
                left = nums[j]
                continue
            for k in range(j + 1, n):
                res = max(res, (left - nums[j]) * nums[k])

        return res


s = Solution()
print(s.maximumTripletValue([12, 6, 1, 2, 7]))
print(s.maximumTripletValue([1, 10, 3, 4, 19]))

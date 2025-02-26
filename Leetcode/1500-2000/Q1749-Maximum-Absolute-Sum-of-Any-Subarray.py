from itertools import accumulate
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum , max_sum = 0, 0
        cur = 0
        res = 0

        for num in nums:
            cur += num
            res = max(res, abs(cur - min_sum), abs(cur - max_sum))
            max_sum = max(max_sum, cur)
            min_sum = min(min_sum, cur)
        return res

    def maxAbsoluteSum2(self, nums: List[int]) -> int:
        max_sum, max_cur = 0, 0
        min_sum, min_cur = 0, 0

        for num in nums:
            max_cur = max(max_cur + num, 0)
            max_sum = max(max_sum, max_cur)

            min_cur = min(min_cur + num, 0)
            min_sum = min(min_sum, min_cur)
        return max(max_sum, -min_sum)

    def maxAbsoluteSum3(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))
        return max(s) - min(s)

    def maxAbsoluteSum3(self, nums: List[int]) -> int:
        accumulated_sum = [0]

        for num in nums:
            accumulated_sum.append(num + accumulated_sum[-1])
        return max(accumulated_sum) - min(accumulated_sum)


s = Solution()
print(s.maxAbsoluteSum([1, -3, 2, 3, -4]))
print(s.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))
print(s.maxAbsoluteSum2([1, -3, 2, 3, -4]))
print(s.maxAbsoluteSum2([2, -5, 1, -4, 3, -2]))
print(s.maxAbsoluteSum3([1, -3, 2, 3, -4]))
print(s.maxAbsoluteSum3([2, -5, 1, -4, 3, -2]))

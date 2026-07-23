from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        left_sum = 0
        right_sum = sum(nums)
        for num in nums:
            right_sum -= num
            res.append(abs(right_sum - left_sum))
            left_sum += num
        return res


s = Solution()
print(s.leftRightDifference(nums=[10, 4, 8, 3]))
print(s.leftRightDifference(nums=[1]))

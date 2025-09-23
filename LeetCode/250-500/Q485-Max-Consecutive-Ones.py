from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
                res = max(res, count)
        return res


s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))

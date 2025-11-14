from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum1 = 0
        sum2 = 0
        for num in nums:
            if num < 10:
                sum1 += num
            else:
                sum2 += num
        return sum1 != sum2


s = Solution()
print(s.canAliceWin(nums=[1, 2, 3, 4, 10]))
print(s.canAliceWin(nums=[1, 2, 3, 4, 5, 14]))
print(s.canAliceWin(nums=[5, 5, 5, 25]))

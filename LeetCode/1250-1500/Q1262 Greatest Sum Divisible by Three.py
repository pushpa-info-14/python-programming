import math
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        rem1 = []
        rem2 = []
        res = 0
        for num in nums:
            res += num
            if num % 3 == 1:
                rem1.append(num)
            elif num % 3 == 2:
                rem2.append(num)
        rem1.sort()
        rem2.sort()

        if res % 3 == 1:
            x = math.inf
            if len(rem1):
                x = min(x, rem1[0])
            if len(rem2) > 1:
                x = min(x, rem2[0] + rem2[1])
            res -= x
        elif res % 3 == 2:
            x = math.inf
            if len(rem1) > 1:
                x = min(x, rem1[0] + rem1[1])
            if len(rem2):
                x = min(x, rem2[0])
            res -= x

        return res


s = Solution()
print(s.maxSumDivThree(nums=[3, 6, 5, 1, 8]))
print(s.maxSumDivThree(nums=[4]))
print(s.maxSumDivThree(nums=[1, 2, 3, 4, 4]))
print(s.maxSumDivThree(nums=[2, 6, 2, 2, 7]))

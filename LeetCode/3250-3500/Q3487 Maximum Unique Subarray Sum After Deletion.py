from collections import Counter
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        freq = Counter(nums)
        unique_nums = sorted(freq.keys())

        if unique_nums[-1] < 0:
            return unique_nums[-1]
        else:
            res = 0
            for num in unique_nums:
                if num > 0:
                    res += num
            return res


s = Solution()
print(s.maxSum(nums=[1, 2, 3, 4, 5]))
print(s.maxSum(nums=[1, 1, 0, 1, 1]))
print(s.maxSum(nums=[1, 2, -1, -2, 1, 0, -1]))
print(s.maxSum(nums=[-100]))
print(s.maxSum(nums=[-20, 20]))

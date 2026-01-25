from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        j = len(nums) - 1
        while i <= j:
            x = nums[i]
            y = nums[j]
            if abs(x) < abs(y):
                res.append(y * y)
                j -= 1
            else:
                res.append(x * x)
                i += 1
        return res[::-1]


s = Solution()
print(s.sortedSquares(nums=[-4, -1, 0, 3, 10]))
print(s.sortedSquares(nums=[-7, -3, 2, 3, 11]))

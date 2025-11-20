from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        res = 0
        for num in nums:
            res += max_num - num
        return res


s = Solution()
print(s.minMoves(nums=[2, 1, 3]))
print(s.minMoves(nums=[4, 4, 5]))

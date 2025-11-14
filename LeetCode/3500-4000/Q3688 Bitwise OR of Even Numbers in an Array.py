from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if num & 1 == 0:
                res |= num
        return res


s = Solution()
print(s.evenNumberBitwiseORs(nums=[1, 2, 3, 4, 5, 6]))
print(s.evenNumberBitwiseORs(nums=[7, 9, 11]))
print(s.evenNumberBitwiseORs(nums=[1, 8, 16]))

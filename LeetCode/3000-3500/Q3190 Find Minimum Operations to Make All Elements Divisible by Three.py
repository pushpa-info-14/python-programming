from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if num % 3:
                res += 1
        return res


s = Solution()
print(s.minimumOperations(nums=[1, 2, 3, 4]))
print(s.minimumOperations(nums=[3, 6, 9]))

from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(1, len(nums)):
            for num in range(nums[i - 1] + 1, nums[i]):
                res.append(num)
        return res


s = Solution()
print(s.findMissingElements(nums=[1, 4, 2, 5]))
print(s.findMissingElements(nums=[7, 8, 6, 9]))
print(s.findMissingElements(nums=[5, 1]))

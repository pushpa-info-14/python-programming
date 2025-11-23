from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                res.append(num)
            nums[num - 1] = -nums[num - 1]

        return res


s = Solution()
print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(s.findDuplicates([1, 1, 2]))
print(s.findDuplicates([1]))

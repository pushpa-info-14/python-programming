from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        map = [0 for i in range(len(nums) + 1)]

        for num in nums:
            map[num] = 1

        res = []
        for i in range(1, len(nums) + 1):
            if map[i] == 0:
                res.append(i)
        return res

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            if nums[nums[i] - 1] == nums[i]:
                i += 1
            else:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

        res = []
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res

    def findDisappearedNumbers3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            index = abs(nums[i])
            if nums[index - 1] > 0:
                nums[index - 1] = -nums[index - 1]
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        return res


s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(s.findDisappearedNumbers([1, 1]))
print(s.findDisappearedNumbers2([4, 3, 2, 7, 8, 2, 3, 1]))
print(s.findDisappearedNumbers2([1, 1]))
print(s.findDisappearedNumbers2([2, 2]))
print(s.findDisappearedNumbers3([4, 3, 2, 7, 8, 2, 3, 1]))
print(s.findDisappearedNumbers3([1, 1]))
print(s.findDisappearedNumbers3([2, 2]))

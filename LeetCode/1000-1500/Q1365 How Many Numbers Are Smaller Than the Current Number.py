from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_copy = nums.copy()
        nums_copy.sort()
        mp = {}
        cur = 0
        i = 0
        while i < n:
            mp[nums_copy[i]] = cur
            while i + 1 < n and nums_copy[i] == nums_copy[i + 1]:
                i += 1
            cur = i + 1
            i += 1
        res = []
        for num in nums:
            res.append(mp[num])
        return res


s = Solution()
print(s.smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))
print(s.smallerNumbersThanCurrent(nums=[6, 5, 4, 8]))
print(s.smallerNumbersThanCurrent(nums=[7, 7, 7, 7]))

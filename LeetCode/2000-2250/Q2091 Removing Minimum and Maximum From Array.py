from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_index = 0
        max_index = 0
        for i in range(n):
            if nums[min_index] > nums[i]:
                min_index = i
            if nums[max_index] < nums[i]:
                max_index = i
        l = min(min_index, max_index)
        r = max(min_index, max_index)
        return min(r + 1, n - l, l + (n - r) + 1)


s = Solution()
print(s.minimumDeletions(nums=[2, 10, 7, 5, 4, 1, 8, 6]))
print(s.minimumDeletions(nums=[0, -4, 19, 1, 8, -2, -3, 5]))
print(s.minimumDeletions(nums=[101]))
print(s.minimumDeletions(nums=[42, -75]))
print(s.minimumDeletions(nums=[-14, 61, 29, -18, 59, 13, -67, -16, 55, -57, 7, 74]))

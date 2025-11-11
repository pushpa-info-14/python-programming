from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        return nums2[0] - nums1[0]


s = Solution()
print(s.addedInteger(nums1=[2, 6, 4], nums2=[9, 7, 5]))
print(s.addedInteger(nums1=[10], nums2=[5]))
print(s.addedInteger(nums1=[1, 1, 1, 1], nums2=[1, 1, 1, 1]))

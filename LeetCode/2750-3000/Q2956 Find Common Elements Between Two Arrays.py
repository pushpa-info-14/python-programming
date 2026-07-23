from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res1 = 0
        res2 = 0
        set1 = set(nums1)
        set2 = set(nums2)
        for x in nums1:
            if x in set2:
                res1 += 1
        for x in nums2:
            if x in set1:
                res2 += 1
        return [res1, res2]


s = Solution()
print(s.findIntersectionValues(nums1=[2, 3, 2], nums2=[1, 2]))
print(s.findIntersectionValues(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]))
print(s.findIntersectionValues(nums1=[3, 4, 2, 3], nums2=[1, 5]))
